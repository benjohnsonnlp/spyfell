# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20170417_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='current_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Location'),
        ),
    ]
