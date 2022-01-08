from django.shortcuts import render


def about_view(request):
    context = {}
    return render(request, "../templates/app_pages/about.html", context)
