# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0016_auto_20170822_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='civil_status',
            field=models.CharField(blank=True, choices=[('S', 'Soltero/a'), ('P', 'Con pareja'), ('C', 'Casado/a'), ('D', 'Divorciado/a (separado/a)'), ('V', 'Viudo/a')], max_length=2),
        ),
        migrations.AlterField(
            model_name='subject',
            name='gender',
            field=models.CharField(blank=True, choices=[('0', 'Mujer'), ('1', 'Hombre'), ('2', 'Otro')], max_length=2),
        ),
        migrations.AlterField(
            model_name='subject',
            name='last_studies',
            field=models.CharField(blank=True, choices=[('P', 'Primaria'), ('S', 'Secundaria'), ('B', 'Bachillerato'), ('FM', 'Formación profesional media'), ('FS', 'Formación profesional superior'), ('U', 'Universidad')], max_length=2),
        ),
    ]