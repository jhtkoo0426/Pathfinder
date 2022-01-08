from django.shortcuts import render
from .models import Station


# Create your views here.
def station_detail_view(request):
    obj = Station.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "../templates/app_pages/stn_detail.html", context)
