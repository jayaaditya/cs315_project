# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180424_0722'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='enrolled',
            index=models.Index(fields=['rollno'], name='main_enroll_rollno__cf7efe_idx'),
        ),
        migrations.AddIndex(
            model_name='enrolled',
            index=models.Index(fields=['ccode'], name='main_enroll_ccode_i_6e716f_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['rollno'], name='main_studen_rollno_52d42b_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['name'], name='main_studen_name_d24c58_idx'),
        ),
    ]
