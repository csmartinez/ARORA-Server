# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import LocationReport
from .models import UserInteraction
from .models import MoodReport
from .models import ThoughtDistortionReport
from rest_framework import viewsets
from .serializers import LocationReportSerializer
from .serializers import UserInteractionSerializer
from .serializers import MoodReportSerializer
from .serializers import ThoughtDistortionReportSerializer

# Create your views here.
class LocationReport(viewsets.ModelViewSet):
    queryset = LocationReport.objects.all()
    serializer_class = LocationReportSerializer

class UserInteraction(viewsets.ModelViewSet):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer

class MoodReport(viewsets.ModelViewSet):
    queryset = MoodReport.objects.all()
    serializer_class = MoodReportSerializer

class ThoughtDistortionReport(viewsets.ModelViewSet):
    queryset = ThoughtDistortionReport.objects.all()
    serializer_class = ThoughtDistortionReportSerializer
