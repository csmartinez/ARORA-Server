# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Quest
from . models import QuestStatus
from . models import QuestReport

# Register your models here.
admin.site.register(Quest)
admin.site.register(QuestStatus)
admin.site.register(QuestReport)
