# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Quest
from rest_framework import viewsets
from .serializers import QuestSerializer

# Create your views here.

class Quest(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
