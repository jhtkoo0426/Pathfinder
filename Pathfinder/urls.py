"""Pathfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import *
from about.views import about_view
from stations.views import station_detail_view


# TODO: Convert the function views to Class-based views
urlpatterns = [
    # path('search/', search_view, name='search'),
    path('', search_view, name='home'),
    path('about/', about_view, name='about'),
    path('stations/', station_detail_view, name='stations'),
    path(r'^ajax/get_response/$', getAlgorithmResults, name='get_response')
]
