# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import LocationReport
from . models import UserInteraction
from . models import MoodReport
from . models import ThoughtDistortionReport

# Register your models here.
admin.site.register(LocationReport)
admin.site.register(UserInteraction)
admin.site.register(MoodReport)
admin.site.register(ThoughtDistortionReport)
