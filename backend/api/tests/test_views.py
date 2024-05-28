from django.test import TestCase

from api.models import Location


class GetWeatherViewTest(TestCase):

    def test_view_does_not_allow_get_request(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 405)

    def test_view_with_no_request_body(self):
        response = self.client.post("/api/")
        self.assertEqual(response.status_code, 400)

    def test_get_weather_view_with_correct_request(self):
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)

    def test_get_weather_view_with_incorrect_request(self):
        response = self.client.post("/api/", data={"place": "Kathmandu"})
        self.assertEqual(response.status_code, 400)

    def test_get_weather_view_with_empty_request(self):
        response = self.client.post("/api/", data={"location": ""})
        self.assertEqual(response.status_code, 500)

    def test_get_weather_twice(self):
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/api/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)


class FetchWeatherViewTest(TestCase):

    def test_fetch_view_does_not_allow_get_request(self):
        response = self.client.get("/api/fetch/")
        self.assertEqual(response.status_code, 405)

    def test_fetch_view_with_no_request_body(self):
        response = self.client.post("/api/fetch/")
        self.assertEqual(response.status_code, 400)

    def test_get_weather_view_with_empty_request(self):
        response = self.client.post("/api/fetch/", data={"location": ""})
        self.assertEqual(response.status_code, 500)

    def test_fetch__weather_view_with_correct_request(self):
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)

    def test_fetch__weather_view_with_incorrect_request(self):
        response = self.client.post("/api/fetch/", data={"place": "Kathmandu"})
        self.assertEqual(response.status_code, 400)

    def test_fetch__weather_twice(self):
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/api/fetch/", data={"location": "Kathmandu"})
        self.assertEqual(response.status_code, 200)
