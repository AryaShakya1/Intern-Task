from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_weather_data, name="get_weather"),
    path("fetch/", views.fetch_weather_data, name="post_weather"),
]
