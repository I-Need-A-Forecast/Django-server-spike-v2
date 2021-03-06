# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CurrentObservation(models.Model):
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

    class Meta:
        managed = False
        db_table = 'current_observation'
        ordering = ['-obsdate', '-obstime', 'station_id']


class DbTestsPerson(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'db_tests_person'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'
