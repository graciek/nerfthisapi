# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-27 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_map_map_stages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='role',
            field=models.CharField(choices=[('OF', 'Offense'), ('DE', 'Defense'), ('TA', 'Tank'), ('SU', 'Support'), ('DA', 'Damage')], max_length=2),
        ),
    ]
