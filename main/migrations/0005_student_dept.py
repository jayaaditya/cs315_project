# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180413_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='main.department'),
        ),
    ]
