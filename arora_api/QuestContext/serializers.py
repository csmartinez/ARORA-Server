# posts/serializers.py
from rest_framework import serializers
from . import models


class QuestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'QuestTypeId', 'QuestStatus',)
        model = models.Quest
