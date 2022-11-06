from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin)
from .models import *
from .serializers import *


class BattleViewSet(ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class PokemonViewSet(ModelViewSet):
    queryset = BasePokemon.objects.select_related("ability_1", "ability_2", "ability_3").all()
    serializer_class = BasePokemonSerializer


class AbilityViewSet(ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

