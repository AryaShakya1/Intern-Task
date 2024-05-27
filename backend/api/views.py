from .services import fetch_weather, get_weather
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .helpers import logging


@api_view(["POST"])
def get_weather_data(request):
    try:
        if not request:
            return Response("Request was Empty", status=status.HTTP_400_BAD_REQUEST)
        if not request.data:
            return Response(
                "Request cannot be Empty", status=status.HTTP_400_BAD_REQUEST
            )
        if "location" not in request.data:
            return Response(
                "Location was not provided", status=status.HTTP_400_BAD_REQUEST
            )
        location = request.data["location"]
        response = get_weather(location=location)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"Error:: get_weather_data :: exception {e}")
        return Response(
            "Error: Unable to get weather data",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def fetch_weather_data(request):
    try:
        if not request:
            return Response(
                "Request cannot be Empty", status=status.HTTP_400_BAD_REQUEST
            )
        if not request.data:
            return Response(
                "Request cannot be Empty", status=status.HTTP_400_BAD_REQUEST
            )
        if "location" not in request.data:
            return Response(
                "Location was not provided", status=status.HTTP_400_BAD_REQUEST
            )
        location = request.data["location"]
        response = fetch_weather(location=location)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"Error:: get_weather_data :: exception {e}")
        return Response(
            "Error: Unable to get weather data",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
