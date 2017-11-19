# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-25 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171119_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='heroes'),
        ),
        migrations.AlterField(
            model_name='map',
            name='image',
            field=models.ImageField(blank=True, upload_to='maps'),
        ),
    ]