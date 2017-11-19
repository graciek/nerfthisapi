# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin


@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    search_fields = (
        'name', 'role'
    )
    list_display = (
        'name', 'role', 'affiliation', 'difficulty'
    )
    list_filter = ('role', 'affiliation', 'difficulty')


@admin.register(models.Ability)
class AbilityAdmin(admin.ModelAdmin):
    search_fields = (
        'name', 'hero__name'
    )
    list_display = (
        'name', 'hero', 'is_ultimate'
    )
    list_filter = ('hero', 'is_ultimate',)


@admin.register(models.Line)
class LineAdmin(admin.ModelAdmin):
    search_fields = (
        'voice_line', 'hero__name'
    )
    list_display = (
        'voice_line', 'hero'
    )
    list_filter = ('hero',)


@admin.register(models.Map)
class MapAdmin(admin.ModelAdmin):
    search_fields = (
        'name', 'location', 'game_mode'
    )
    list_display = (
        'name', 'location', 'game_mode'
    )
    list_filter = ('game_mode',)
