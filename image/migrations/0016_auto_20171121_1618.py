# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0015_auto_20171121_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_date_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Date of the Lecture'),
        ),
    ]
