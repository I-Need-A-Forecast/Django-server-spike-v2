import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return ('{ ' +
            "First Name: " + self.first_name + ' ' +
            "Last Name: " + self.last_name +
            ' }')
            
class CurrentObservation(models.Model):

    # Fields
    observation_id = models.AutoField(db_column='Observation_ID', primary_key=True)  # Field name made lowercase.
    obsdate = models.DateField(db_column='obsDate')  # Field name made lowercase.
    obstime = models.TimeField(db_column='obsTime')  # Field name made lowercase.
    credit = models.CharField(max_length=255, blank=True, null=True)
    credit_url = models.CharField(db_column='credit_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suggested_pickup = models.CharField(max_length=255, blank=True, null=True)
    suggested_pickup_period = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    station_id = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    observation_time = models.CharField(max_length=255, blank=True, null=True)
    observation_time_rfc822 = models.CharField(max_length=255, blank=True, null=True)
    weather = models.CharField(max_length=255, blank=True, null=True)
    temperature_string = models.CharField(max_length=255, blank=True, null=True)
    temp_f = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    temp_c = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    water_temp_f = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    water_temp_c = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    relative_humidity = models.IntegerField(blank=True, null=True)
    wind_string = models.CharField(max_length=255, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, blank=True, null=True)
    wind_degrees = models.IntegerField(blank=True, null=True)
    wind_mph = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    wind_gust_mph = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    wind_kt = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    wind_gust_kt = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pressure_string = models.CharField(max_length=255, blank=True, null=True)
    pressure_mb = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pressure_in = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pressure_tendency_mb = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pressure_tendency_in = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dewpoint_string = models.CharField(max_length=255, blank=True, null=True)
    dewpoint_f = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dewpoint_c = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    heat_index_string = models.CharField(max_length=255, blank=True, null=True)
    heat_index_f = models.IntegerField(blank=True, null=True)
    heat_index_c = models.IntegerField(blank=True, null=True)
    windchill_string = models.CharField(max_length=255, blank=True, null=True)
    windchill_f = models.IntegerField(blank=True, null=True)
    windchill_c = models.IntegerField(blank=True, null=True)
    visibility_mi = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    wave_height_m = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    wave_height_ft = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dominant_period_sec = models.IntegerField(blank=True, null=True)
    average_period_sec = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    mean_wave_dir = models.CharField(max_length=255, blank=True, null=True)
    mean_wave_degrees = models.IntegerField(blank=True, null=True)
    tide_ft = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    steepness = models.CharField(max_length=255, blank=True, null=True)
    water_column_height = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    surf_height_ft = models.CharField(max_length=255, blank=True, null=True)
    swell_dir = models.CharField(max_length=255, blank=True, null=True)
    swell_degrees = models.IntegerField(blank=True, null=True)
    swell_period = models.CharField(max_length=255, blank=True, null=True)
    icon_url_base = models.CharField(max_length=255, blank=True, null=True)
    icon_name = models.CharField(max_length=255, blank=True, null=True)
    two_day_history_url = models.CharField(max_length=255, blank=True, null=True)
    icon_url_name = models.CharField(max_length=255, blank=True, null=True)
    ob_url = models.CharField(max_length=255, blank=True, null=True)
    disclaimer_url = models.CharField(max_length=255, blank=True, null=True)
    copyright_url = models.CharField(max_length=255, blank=True, null=True)
    privacy_policy_url = models.CharField(max_length=255, blank=True, null=True)

    # Metadata
    class Meta:
        managed = False
        db_table = 'current_observation'

    # Methods
    def __repr__(self):
        return str(self.obsdate) + ' ' + str(self.obstime) + ' ' + str(self.temp_f) + ' ' + str(self.station_id)