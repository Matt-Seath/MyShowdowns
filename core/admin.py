from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(BasePokemon)
class BasePokemonAdmin(admin.ModelAdmin):
    list_display = ["name", "tier", "type_1", "type_2", "ability_1", "ability_2", "ability_3"]
    list_editable = ["tier"]


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "match_format", "player_1", "player_2", "victor", "date_created"]
    list_editable = ["match_format"]


@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ["id", "artwork", "front", "front_shiny"]


@admin.register(Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ["name", "sprite"]
    list_editable = ["sprite"]


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "effect"]


@admin.register(CustomPokemon)
class CustomPokemonAdmin(admin.ModelAdmin):
    list_display = ["pokemon", "nickname", "nature", "ability", "evs_hp",
                    "evs_att", "evs_def", "evs_sp_att", "evs_sp_def", "evs_spd",]
    list_editable = ["nickname"]
