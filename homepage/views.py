from django.shortcuts import render
from django.http import JsonResponse
from stations.models import Station
from math import radians, sin, cos, atan2, sqrt
from .forms import SearchStationForm
from .algorithms import Dijkstra


def calculateDistance(lt1, lg1, lt2, lg2):
    lat1, long1, lat2, long2 = radians(lt1), radians(lg1), radians(lt2), radians(lg2)
    delta_lat, delta_long = lat2 - lat1, long2 - long1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_long / 2) ** 2
    distance = 2 * atan2(sqrt(a), sqrt(1 - a)) * 3960.0  # In miles
    return distance


def runDijkstra(vertices, adjList, start, end):
    dijkstra = Dijkstra(vertices, adjList)
    parents, visited = dijkstra.find_route(start, end)
    path = dijkstra.generate_path(parents, start, end)
    name_path = ' -> '.join([(Station.objects.get(id=i)).name for i in path])
    return name_path, path


# Auxiliary function to check if the stations the user entered exist, and return the station objects
# and corresponding error messages.
def checkValid(queried_objects):
    return_objects = []
    for i in queried_objects:
        try:
            target = Station.objects.get(name=i)
            return_objects.append(target)
        except Station.DoesNotExist:
            return_objects.append(None)

    if return_objects[0] is not None:
        found_start = return_objects[0]
        error_start = None
    else:
        found_start = None
        error_start = f"The station {queried_objects[0]} does not exist."
    if return_objects[1] is not None:
        found_end = return_objects[1]
        error_end = None
    else:
        found_end = None
        error_end = f"The station {queried_objects[1]} does not exist."
    return found_start, found_end, error_start, error_end


# Ajax function to return the results of executing algorithms.
def getAlgorithmResults(request):
    user_start = request.GET.get('user_start')
    user_end = request.GET.get('user_end')
    found_start, found_end, error_start, error_end = checkValid([user_start, user_end])
    if found_start is None or found_end is None:
        data = {
            'calculated_distance': None,
            'calculated_name_path': None,
            'calculated_raw_path': None,
            'error_start': error_start,
            'error_end': error_end
        }
        return JsonResponse(data)
    else:
        distance = calculateDistance(found_start.lat, found_start.lng, found_end.lat, found_end.lng)
        vertices = (i for i in range(len(Station.objects.all())))
        adjList = {}
        for i in range(1, len(Station.objects.all())):
            item = Station.objects.get(id=i)
            adj = item.adjacencyList
            adjList[i] = adj

        name_path, raw_path = runDijkstra(vertices, adjList, found_start.id, found_end.id)
        data = {
            'calculated_distance': distance,
            'calculated_name_path': name_path,
            'calculated_raw_path': raw_path,
            'error_start': error_start,
            'error_end': error_end
        }
        return JsonResponse(data)


# Pathfinder search view - used for searching and displaying algorithm results.
# Accepts the request and return a response in JSON format.
def search_view(request):
    form = SearchStationForm()
    stations = Station.objects.all()
    context = {
        "form": form,
        "stations": stations
    }
    return render(request, "app_pages/pathfinder.html", context)
