# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-26 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20180523_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='affliation',
            new_name='affiliation',
        ),
    ]
