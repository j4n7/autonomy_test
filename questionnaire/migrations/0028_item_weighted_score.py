# Generated by Django 2.1.3 on 2019-05-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0027_auto_20170928_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='weighted_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]