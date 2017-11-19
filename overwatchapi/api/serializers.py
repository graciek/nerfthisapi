from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    role = serializers.CharField(source='get_role_display')
    sub_roles = serializers.SerializerMethodField()
    abilities = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='apiv1:ability-detail',
        )
    voice_lines = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='apiv1:line-detail',
        source='lines')

    class Meta:
        avatar = serializers.URLField(source='avatar.url', read_only=True)
        model = models.Character
        fields = ('id', 'name', 'real_name', 'description', 'avatar', 'age',
                  'nationality', 'height', 'occupation', 'affiliation',
                  'base_of_operations', 'role', 'sub_roles', 'difficulty',
                  'stats', 'abilities', 'voice_lines')

    def get_sub_roles(self, obj):
        sub_roles = models.Character.get_sub_role_display(obj)
        return sub_roles.split(', ')


class NestedCharacterSerializer(CharacterSerializer):
    # Character data to be displayed inside other serializers
    url = serializers.HyperlinkedIdentityField(
        view_name='apiv1:character-detail')

    class Meta:
        model = models.Character
        fields = ('id', 'name', 'url')


class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    hero = NestedCharacterSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='apiv1:ability-detail')

    class Meta:
        model = models.Ability
        fields = ('id', 'name', 'description', 'is_ultimate',
                  'hero', 'icon', 'stats', 'url')


class CharacterAbilitySerializer(serializers.HyperlinkedModelSerializer):
    # Ability data belonging to a Character
    url = serializers.HyperlinkedIdentityField(
        view_name='apiv1:ability-detail')

    class Meta:
        model = models.Ability
        fields = ('id', 'name', 'description', 'is_ultimate',
                  'icon', 'stats', 'url')


class MapSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='apiv1:map-detail')
    game_mode = serializers.CharField(source='get_game_mode_display')

    class Meta:
        model = models.Map
        fields = ('id', 'name', 'game_mode', 'location', 'description',
                  'image', 'stages', 'url')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    hero = NestedCharacterSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='apiv1:line-detail')

    class Meta:
        model = models.Line
        fields = ('id', 'voice_line', 'english_translation', 'url', 'hero')


class CharacterLineSerializer(serializers.HyperlinkedModelSerializer):
    # Line data belonging to a Character
    url = serializers.HyperlinkedIdentityField(view_name='apiv1:line-detail')

    class Meta:
        model = models.Line
        fields = ('id', 'voice_line', 'english_translation', 'url')


class NestedLineSerializer(LineSerializer):
    # Line data to be displayed inside other serializers
    class Meta:
        model = models.Line
        fields = ('id', 'voice_line', 'url',
                  'is_ultimate', 'icon', 'stats', 'url')
