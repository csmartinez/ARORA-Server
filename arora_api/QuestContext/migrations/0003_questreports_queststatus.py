# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestContext', '0002_auto_20181112_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.IntegerField()),
                ('QuestStartedAt', models.DateTimeField(auto_now_add=True)),
                ('QuestCompletedAt', models.DateTimeField(auto_now=True)),
                ('QuestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='QuestContext.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='QuestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestStatusDescription', models.TextField()),
            ],
        ),
    ]