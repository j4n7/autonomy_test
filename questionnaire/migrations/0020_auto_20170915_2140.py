# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 19:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0019_auto_20170906_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='city',
            new_name='current_city',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='country',
            new_name='current_country',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='school_years',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='user_ip',
        ),
        migrations.AddField(
            model_name='subject',
            name='home_city',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AddField(
            model_name='subject',
            name='home_country',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AddField(
            model_name='subject',
            name='sex',
            field=models.CharField(choices=[('0', 'Mujer'), ('1', 'Hombre')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='total_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='age',
            field=models.IntegerField(default=27, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(99)]),
            preserve_default=False,
        ),
    ]
