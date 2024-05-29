import datetime
from django.test import TestCase

from api.models import Location, RealTimeWeather
from api.serializers import RealTimeWeatherSerializer


class GetWeatherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.location = Location.objects.create(
            lat=27.72,
            lon=85.32,
            name="Kathmandu",
            region="",
            country="Nepal",
            tz_id="Asia/Kathmandu",
            localtime_epoch=1716884072,
            localtime="2024-05-28 13:59",
        )
        cls.weather = RealTimeWeather.objects.create(
            location=cls.location,
            last_updated=datetime.datetime.now(),
            last_updated_epoch=1716884072,
            temp_c=29.66,
            temp_f=98.44,
            feelslike_c=28.56,
            feelslike_f=97.23,
            condition={},
            wind_mph=15.49,
            wind_kph=15.49,
            wind_degree=21,
            wind_dir="NW",
            pressure_mb=15.49,
            pressure_in=15.49,
            precip_mm=15.49,
            precip_in=15.49,
            humidity=19,
            cloud=20,
            is_day=1,
            uv=15.49,
            gust_mph=15.49,
            gust_kph=15.49,
        )

    def test_view_does_not_allow_get_request(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 405)

    def test_view_with_no_request_body(self):
        response = self.client.post("/api/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), "Request cannot be Empty")

    def test_get_weather_view_with_correct_request(self):
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        data = RealTimeWeatherSerializer(self.weather).data
        self.assertEqual(response.json(), data)

    def test_get_weather_view_with_incorrect_request(self):
        response = self.client.post("/api/", data={"place": "Kathmandu"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), "Location was not provided")

    def test_get_weather_view_with_empty_request(self):
        response = self.client.post("/api/", data={"location": ""})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), "Error: Unable to get weather data")

    def test_get_weather_twice(self):
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        data = RealTimeWeatherSerializer(self.weather).data
        self.assertEqual(response.json(), data)
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), data)
        self.assertEqual(RealTimeWeather.objects.count(), 1)


class FetchWeatherViewTest(TestCase):

    def test_fetch_view_does_not_allow_get_request(self):
        response = self.client.get("/api/fetch/")
        self.assertEqual(response.status_code, 405)

    def test_fetch_view_with_no_request_body(self):
        response = self.client.post("/api/fetch/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), "Request cannot be Empty")

    def test_get_weather_view_with_empty_request(self):
        response = self.client.post("/api/fetch/", data={"location": ""})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), "Error: Unable to get weather data")

    def test_fetch_weather_view_with_correct_request(self):
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)

    def test_fetch_weather_view_with_incorrect_request(self):
        response = self.client.post("/api/fetch/", data={"place": "Kathmandu"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), "Location was not provided")

    def test_fetch_weather_twice(self):
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(RealTimeWeather.objects.count(), 2)
