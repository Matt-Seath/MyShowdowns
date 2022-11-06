from rest_framework import serializers
from .models import *


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = ["id", "name"]

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = [
            "id", "title", "link", "match_format", "gametype", 
            "player_1", "player_2", "victor", "description",
            "p1_pk_1", "p1_pk_2", "p1_pk_3", "p1_pk_4", "p1_pk_5",
            "p1_pk_6", "p2_pk_1", "p2_pk_2", "p2_pk_3", "p2_pk_4",
            "p2_pk_5", "p2_pk_6"
        ]


class BasePokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePokemon
        fields = [
            "id", "name", "type_1", "type_2", "ability_1", "ability_2",
            "ability_3", "artwork", "base_hp", "base_att", "base_def",
            "base_sp_att", "base_sp_def", "base_spd", "tier"
        ]


class CustomPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPokemon
        fields = [
            "id", "pokemon", "nickname", "nature", "ability", 
            "ivs_hp", "ivs_att", "ivs_def", "ivs_sp_att", "ivs_sp_def",
            "ivs_spd", "evs_hp", "evs_att", "evs_def", "evs_sp_att", 
            "evs_sp_def", "evs_spd"
        ]


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ["id", "artwork", "front", "front_shiny"]


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ["id", "name", "effect"]
