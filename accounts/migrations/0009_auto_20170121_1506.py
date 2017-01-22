# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170121_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensoruser', to=settings.AUTH_USER_MODEL),
        ),
    ]