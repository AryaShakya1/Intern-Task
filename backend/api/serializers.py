from rest_framework import serializers
from .models import Location, RealTimeWeather


class RequestSerializer(serializers.Serializer):
    location = serializers.CharField()


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class RealTimeWeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    class Meta:
        model = RealTimeWeather
        fields = "__all__"
