import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from stations.models import Station
from math import radians, sin, cos, atan2, sqrt
import utm
from .forms import SearchStationForm


def calculateDistance(lt1, lg1, lt2, lg2):
    lat1, long1, lat2, long2 = radians(lt1), radians(lg1), radians(lt2), radians(lg2)
    delta_lat, delta_long = lat2 - lat1, long2 - long1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_long / 2) ** 2
    distance = 2 * atan2(sqrt(a), sqrt(1 - a)) * 3960.0  # In miles
    return distance


def latlngToXY(lat, lng):
    result = utm.from_latlon(lat, lng)      # In the form of (x, y, UTM Zone)
    return result[0], result[1]


# View to accept the request and return a respons in JSON format.
def search_view(request):
    form = SearchStationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user_start = form.cleaned_data.get("start_station")
            user_end = form.cleaned_data.get("end_station")
            found_start = Station.objects.get(name=user_start)
            found_end = Station.objects.get(name=user_end)
            distance = calculateDistance(found_start.lat, found_start.lng, found_end.lat, found_end.lng)

            context = {
                "user_start": user_start,
                "user_end": user_end,
                "distance": distance,
                "form": form,
                "error": None,
            }
            return render(request, "app_pages/pathfinder.html", context)
    else:
        form = SearchStationForm()
        return render(request, "app_pages/pathfinder.html", {'form': form})


# Pathfinder homepage view - used for searching and displaying algorithm results.
def home_view(request, *args, **kwargs):
    stations = Station.objects.all()
    context = {
        "db": stations,
    }

    # Return a template "pathfinder.html" instead of an HttpResponse.
    return render(request, "app_pages/pathfinder.html", context)

