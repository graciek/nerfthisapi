# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_character_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_mode', models.CharField(choices=[('AS', 'Assault'), ('ES', 'Escort'), ('HY', 'Hybrid'), ('CO', 'Control'), ('AR', 'Arcade'), ('EV', 'Event'), ('AR', 'Arena'), ('DM', 'Death Match')], max_length=2)),
                ('location', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
    ]