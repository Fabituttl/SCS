# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170121_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sensor_measure',
            new_name='sensormeasure',
        ),
    ]
