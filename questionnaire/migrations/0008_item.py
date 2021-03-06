# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_situation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=46)),
                ('user_ip', models.CharField(max_length=46)),
                ('situation_n', models.CharField(max_length=2)),
                ('item_n', models.CharField(max_length=2)),
                ('latency', models.CharField(max_length=32)),
            ],
        ),
    ]
