from rest_framework import serializers
from .models import *


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = ["id", "name"]

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["id", "title", "link", "match_format", "player_1", "player_2", "victor"]


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ["id", "title"]


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["id", "name", "dex_number", "type_1", "type_2"]

