# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20170418_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_spy',
            field=models.BooleanField(default=False),
        ),
    ]
