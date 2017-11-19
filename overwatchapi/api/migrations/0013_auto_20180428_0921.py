# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-28 09:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180428_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='hero',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='api.Character'),
        ),
        migrations.AlterField(
            model_name='line',
            name='hero',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='api.Character'),
        ),
    ]
