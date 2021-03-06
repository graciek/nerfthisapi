# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-26 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180426_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('icon', models.ImageField(blank=True, upload_to='abilities')),
                ('is_ultimate', models.BooleanField(default=False)),
                ('hero', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Character')),
            ],
        ),
    ]
