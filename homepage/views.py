from django.shortcuts import render
from stations.models import Station
from math import radians, sin, cos, atan2, sqrt


def calculateDistance(lt1, lg1, lt2, lg2):
    lat1, long1, lat2, long2 = radians(lt1), radians(lg1), radians(lt2), radians(lg2)
    delta_lat, delta_long = lat2 - lat1, long2 - long1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_long / 2) ** 2
    distance = 2 * atan2(sqrt(a), sqrt(1 - a)) * 3960.0  # In miles
    return distance


# Homepage View
def home_view(request, *args, **kwargs):
    stations = Station.objects.all()

    start, end = stations.get(id=152), stations.get(id=516)
    distance = calculateDistance(start.lat, start.lng, end.lat, end.lng)
    results = [start.lat, start.lng, end.lat, end.lng]

    context = {
        "db": stations,
        "result": results,
        "distance": distance
    }

    # Return a template "pathfinder.html" instead of an HttpResponse.
    return render(request, "app_pages/pathfinder.html", context)
