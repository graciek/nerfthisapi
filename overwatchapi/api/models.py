# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from multiselectfield import MultiSelectField


class Character(models.Model):

    ROLE_CHOICES = (
        ('OF', 'Offense'),
        ('DE', 'Defense'),
        ('TA', 'Tank'),
        ('SU', 'Support'),
    )

    SUBROLE_CHOICES = (
        ('SN', 'Sniper'),
        ('BU', 'Builder'),
        ('HE', 'Healer'),
    )

    name = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=600, blank=True)
    real_name = models.CharField(max_length=60, blank=True)
    avatar = models.FileField(blank=True)
    age = models.PositiveSmallIntegerField(default=0)
    nationality = models.CharField(max_length=60, blank=True)
    height = models.FloatField(blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    base_of_operations = models.CharField(max_length=100, blank=True)
    stats = JSONField(blank=True, null=True)
    difficulty = models.IntegerField(validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ])
    role = models.CharField(choices=ROLE_CHOICES, max_length=2)
    sub_role = MultiSelectField(choices=SUBROLE_CHOICES, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_abilities(self):
        return Ability.objects.filter(hero=self).values(
                'id', 'name', 'description', 'icon', 'stats')

    def get_voice_lines(self):
        return Line.objects.filter(hero=self).values('id', 'voice_line')


class Ability(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=600, blank=True)
    icon = models.ImageField(blank=True, upload_to='abilities')
    is_ultimate = models.BooleanField(default=False)
    hero = models.ForeignKey('Character', related_name='abilities', blank=True)
    stats = JSONField(default=list, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Line(models.Model):

    voice_line = models.CharField(max_length=200)
    hero = models.ForeignKey('Character', related_name='lines', blank=True)
    english_translation = models.CharField(max_length=200, blank=True)


class Map(models.Model):

    GAME_MODE_CHOICES = (
        ('AS', 'Assault'),
        ('ES', 'Escort'),
        ('HY', 'Hybrid'),
        ('CO', 'Control'),
        ('AR', 'Arcade'),
        ('EV', 'Event'),
        ('AR', 'Arena'),
        ('DE', 'Death Match')
    )
    name = models.CharField(max_length=60)
    game_mode = models.CharField(
        choices=GAME_MODE_CHOICES, max_length=2, blank=True)
    location = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(blank=True, upload_to='maps')
    stages = ArrayField(models.CharField(max_length=200, blank=True),
                        blank=True, default=list, null=True, size=10)
