# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-18 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190918_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
    ]
