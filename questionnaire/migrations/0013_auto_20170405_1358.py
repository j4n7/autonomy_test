# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-05 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_auto_20170405_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='age',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='city',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='civil_status',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='country',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='gender',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='last_studies',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='occupation',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='postal_code',
            field=models.CharField(default=2, max_length=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='school_years',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
