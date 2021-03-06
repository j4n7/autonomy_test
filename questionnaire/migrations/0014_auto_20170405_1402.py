# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-05 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0013_auto_20170405_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='city',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='civil_status',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='country',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='gender',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='last_studies',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='occupation',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='postal_code',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='subject',
            name='school_years',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='user_ip',
            field=models.CharField(blank=True, max_length=46),
        ),
    ]
