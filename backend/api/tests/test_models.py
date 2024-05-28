from django.test import TestCase

from api.models import Location


class LocationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Location.objects.create(
            lat=27.72,
            lon=85.32,
            name="Kathmandu",
            region="",
            country="Nepal",
            tz_id="Asia/Kathmandu",
            localtime_epoch=1716884072,
            localtime="2024-05-28 13:59",
        )

    def test_name_label(self):
        location = Location.objects.get(id=1)
        field_label = location._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")