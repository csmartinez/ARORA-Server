# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MoodType(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.title
