# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0020_auto_20171125_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student_roll_no',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='student_roll_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lecture_id',
        ),
    ]
