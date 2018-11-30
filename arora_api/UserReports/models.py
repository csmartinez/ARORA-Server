# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LocationReport(models.Model):
    LocationReportLat = models.DecimalField(max_digits=5, decimal_places=2)
    LocationReportLong = models.DecimalField(max_digits=5, decimal_places=2)
    LocationReportTimestamp = models.DateTimeField()
    # USERID NEEDS TO BE AN FK........
    UserId = models.IntegerField()

    def __int__(self):
        return self.UserId

class UserInteraction(models.Model):
    UserInterationCreatedAt = models.DateTimeField(auto_now_add=True)
    # BOTH BELOW NEED TO BE AN FK........
    InitiatorUserId = models.IntegerField()
    RecieverUserIt = models.IntegerField()

    def __int__(self):
        return self.InitiatorUserId

class MoodReport(models.Model):
    MoodReportCreatedAt = models.DateTimeField(auto_now_add=True)
    # USERID NEEDS TO BE AN FK........
    UserId = models.IntegerField()
    MoodType = models.IntegerField()
    UserText = models.TextField()


    def __int__(self):
        return self.UserText

class ThoughtDistortionReport(models.Model):
    ThoughtDistortionReportCreatedAt = models.DateTimeField(auto_now_add=True)
    # ThoughtDistortionTypeId NEEDS TO BE AN FK........
    ThoughtDistortionTypeId = models.IntegerField()
    # USERID NEEDS TO BE AN FK........
    UserId = models.IntegerField()


    def __int__(self):
        return self.UserText
