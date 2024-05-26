from django.db import models


class Location(models.Model):
    lat = models.DecimalField(decimal_places=2, max_digits=7)
    lon = models.DecimalField(decimal_places=2, max_digits=7)
    name = models.CharField()
    region = models.CharField(default="", blank=True)
    country = models.CharField()
    tz_id = models.CharField()
    localtime_epoch = models.IntegerField()
    localtime = models.CharField()


class RealTimeWeather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    last_updated = models.DateTimeField()
    last_updated_epoch = models.IntegerField()
    temp_c = models.DecimalField(decimal_places=2, max_digits=7)
    temp_f = models.DecimalField(decimal_places=2, max_digits=7)
    feelslike_c = models.DecimalField(decimal_places=2, max_digits=7)
    feelslike_f = models.DecimalField(decimal_places=2, max_digits=7)
    condition = models.JSONField()
    wind_mph = models.DecimalField(decimal_places=2, max_digits=7)
    wind_kph = models.DecimalField(decimal_places=2, max_digits=7)
    wind_degree = models.IntegerField()
    wind_dir = models.CharField()
    pressure_mb = models.DecimalField(decimal_places=2, max_digits=7)
    pressure_in = models.DecimalField(decimal_places=2, max_digits=7)
    precip_mm = models.DecimalField(decimal_places=2, max_digits=7)
    precip_in = models.DecimalField(decimal_places=2, max_digits=7)
    humidity = models.IntegerField()
    cloud = models.IntegerField()
    is_day = models.IntegerField()
    uv = models.DecimalField(decimal_places=2, max_digits=7)
    gust_mph = models.DecimalField(decimal_places=2, max_digits=7)
    gust_kph = models.DecimalField(decimal_places=2, max_digits=7)
