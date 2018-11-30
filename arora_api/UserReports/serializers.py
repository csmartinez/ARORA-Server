# posts/serializers.py
from rest_framework import serializers
from . import models

class LocationReportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'LocationReportLat', 'LocationReportLong','LocationReportTimestamp','UserId')
        model = models.LocationReport

class UserInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'UserInterationCreatedAt', 'InitiatorUserId','RecieverUserIt')
        model = models.UserInteraction

class MoodReportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'MoodReportCreatedAt', 'UserId','MoodType','UserText')
        model = models.MoodReport

class ThoughtDistortionReportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'ThoughtDistortionReportCreatedAt', 'ThoughtDistortionTypeId','UserId')
        model = models.ThoughtDistortionReport
