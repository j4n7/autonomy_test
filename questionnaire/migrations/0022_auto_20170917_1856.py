# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0021_auto_20170915_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='ano_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AddField(
            model_name='subject',
            name='completed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='het_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='pre_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='soc_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='sov_score',
            field=models.IntegerField(default=0),
        ),
    ]