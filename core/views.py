from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin)
from .util import parse_showdown_link
from .models import *
from .serializers import *


class BattleViewSet(ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer

    def create(self, request, *args, **kwargs):
        battle_dict = parse_showdown_link(request.request.link)
        print(battle_dict)
        serializer = BattleSerializer(data=battle_dict)
        serializer.is_valid(raise_exception=True)
        battle = serializer.save()
        serializer = BattleSerializer(battle)
        return Response(serializer.data)


class PokemonViewSet(ModelViewSet):
    queryset = BasePokemon.objects.select_related("ability_1", "ability_2", "ability_3").all()
    serializer_class = BasePokemonSerializer


class AbilityViewSet(ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

