# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_config',
            name='user',
        ),
        migrations.AlterField(
            model_name='main_config',
            name='client_max_body_size',
            field=models.IntegerField(),
        ),
    ]