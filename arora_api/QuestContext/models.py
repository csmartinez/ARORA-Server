# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quest(models.Model):
    QuestTypeId = models.IntegerField()
    QuestStatus = models.IntegerField()

    def __int__(self):
        return self.QuestTypeId

class QuestStatus(models.Model):
    QuestStatusDescription = models.TextField()

    def __str__(self):
        return self.QuestStatusDescription

class QuestReport(models.Model):
    # USERID NEEDS TO BE AN FK........
    UserId = models.IntegerField()
    QuestId = models.ForeignKey(Quest, related_name='quests', on_delete=models.CASCADE)
    QuestStartedAt = models.DateTimeField(auto_now_add=True)
    QuestCompletedAt = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.UserId
