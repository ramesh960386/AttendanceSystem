# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0017_auto_20171123_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_image',
            field=models.ImageField(help_text='Image of Lecture', upload_to='lectures'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(help_text='Student Image', upload_to='students', verbose_name=models.CharField(help_text='Enter Roll Number', max_length=25, primary_key=True, serialize=False)),
        ),
    ]
