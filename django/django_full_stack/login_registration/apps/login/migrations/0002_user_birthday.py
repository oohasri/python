# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-18 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2010-01-01'),
        ),
    ]
