import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name
    def __repr__(self):
        return {
            "First Name:": self.first_name,
            "Last Name:": self.last_name
            }