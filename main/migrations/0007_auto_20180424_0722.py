# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180414_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(db_index=True, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['code'], name='main_course_code_b948e5_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['title'], name='main_course_title_ebecc9_idx'),
        ),
    ]
