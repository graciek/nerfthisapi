from django.views.generic import TemplateView
from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from . import serializers
from .models import Ability, Character, Line, Map


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            HomePage, self).get_context_data(*args, **kwargs)
        context['heroes_count'] = Character.objects.all().count()
        context['abilities_count'] = Ability.objects.all().count()
        context['voice_lines_count'] = Line.objects.all().count()
        context['maps_count'] = Map.objects.all().count()
        return context


class Documentation(TemplateView):
    template_name = 'documentation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            Documentation, self).get_context_data(*args, **kwargs)
        return context


class HeroViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        role = self.request.query_params.get('role', None)
        sub_role = self.request.query_params.get('sub_role', None)
        affiliation = self.request.query_params.get('affiliation', None)
        difficulty = self.request.query_params.get('difficulty', None)
        nationality = self.request.query_params.get('nationality', None)
        if role is not None:
            queryset = queryset.filter(role=role[0:2].upper())
        if sub_role is not None:
            queryset = queryset.filter(
                sub_role__contains=sub_role[0:2].upper())
        if affiliation is not None:
            queryset = queryset.filter(affiliation=affiliation.title())
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty.title())
        if nationality is not None:
            queryset = queryset.filter(nationality=nationality.title())
        return queryset.order_by('id')

    @detail_route(methods=['get'])
    def abilities(self, request, pk=None):
        character = self.get_object()
        serializer = serializers.CharacterAbilitySerializer(
            character.abilities.all(), many=True,
            context={'request': request})
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def voicelines(self, request, pk=None):
        character = self.get_object()
        serializer = serializers.CharacterLineSerializer(
            character.lines.all(), many=True, context={'request': request})
        return Response(serializer.data)


class VoiceLineViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Line.objects.all()
    serializer_class = serializers.LineSerializer

    def get_queryset(self):
        queryset = Line.objects.all()
        hero = self.request.query_params.get('hero', None)
        if hero is not None:
            queryset = queryset.filter(hero__name=hero.title())
        return queryset


class AbilityViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer


class MapViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Map.objects.all()
    serializer_class = serializers.MapSerializer

    def get_queryset(self):
        queryset = Map.objects.all()
        game_mode = self.request.query_params.get('mode', None)
        if game_mode is not None:
            queryset = queryset.filter(role=game_mode[0:2].upper())
        return queryset
