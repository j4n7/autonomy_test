# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0020_auto_20170915_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='total_time',
            field=models.FloatField(default=0),
        ),
    ]
