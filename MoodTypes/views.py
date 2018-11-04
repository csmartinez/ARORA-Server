# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import MoodType
from rest_framework import viewsets
from .serializers import MoodTypeSerializer

# Create your views here.

class MoodTypeList(viewsets.ModelViewSet):
    queryset = MoodType.objects.all()
    serializer_class = MoodTypeSerializer


# For a single instance of a model
class MoodTypeDetail(viewsets.ModelViewSet):
    queryset = MoodType.objects.all()
    serializer_class = MoodTypeSerializer
