# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-23 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_character_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='avatar',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
