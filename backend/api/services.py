import requests
import os

from .models import Location, RealTimeWeather
from .serializers import LocationSerializer, RealTimeWeatherSerializer
from .helpers import logging

base_url = "http://api.weatherapi.com/v1"
apiKey = os.environ.get("WEATHER_API_KEY")


def get_weather(location):
    try:
        locationObject = Location.objects.filter(name=location).first()
        if not locationObject:
            return fetch_weather(location=location)
        weatherObject = (
            RealTimeWeather.objects.filter(location=locationObject)
            .order_by("-last_updated")
            .first()
        )
        weather_serializer = RealTimeWeatherSerializer(weatherObject)
        return weather_serializer.data

    except Exception as e:
        logging.error(e)
        raise e


def fetch_weather(location):
    try:
        response = requests.get(
            base_url + f"/current.json?q={location}&key={apiKey}", timeout=5
        )
        data = response.json()
        locationData = data["location"]
        currentWeatherData = data["current"]
        locationObject = Location.objects.filter(name=location).first()
        if locationObject:
            weather_serializer = RealTimeWeatherSerializer(data=currentWeatherData)
            if weather_serializer.is_valid():
                weather_serializer.save(location=locationObject)
            return weather_serializer.data
        location_serializer = LocationSerializer(data=locationData)
        if location_serializer.is_valid():
            locationInstance = location_serializer.save()
        weather_serializer = RealTimeWeatherSerializer(data=currentWeatherData)
        if weather_serializer.is_valid():
            weather_serializer.save(location=locationInstance)
        return weather_serializer.data
    except (requests.ConnectionError, requests.Timeout) as exception:
        logging.error("Internet is off")
        raise exception
    except Exception as e:
        logging.error(e, type(e))
        raise e
