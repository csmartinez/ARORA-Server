# posts/serializers.py
from rest_framework import serializers
from . import models


class MoodTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('description',)
        model = models.MoodType
