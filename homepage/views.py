from django.shortcuts import render
from django.http import HttpResponse


# Homepage View
def home_view(request, *args, **kwargs):
    context = {
        "my_text": "This is Pathfinder.",
        "my_num": 69,
        "some_list": ["Item 1", "Item 2", "Item 3"],
    }

    # Return a template "home.html" instead of an HttpResponse.
    return render(request, "app_pages/home.html", context)
