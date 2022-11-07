from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Art(models.Model):
    id = models.IntegerField(primary_key=True)
    artwork = models.ImageField(null=True, blank=True)
    front = models.ImageField(null=True, blank=True)
    front_shiny = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)


class Ability(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    effect = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return str(self.name)


class Username(models.Model):
    name = models.CharField(max_length=255)
    sprite = models.ForeignKey(Art, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.name)


class BasePokemon(models.Model):
    TIER_LIST = [
        ("UBER", "Uber"), ("OU", "Overused"), ("UUBL", "Underused Borderline"), ("UU", "Underused"), ("RUBL", "Rarelyused Borderline"),
        ("RU", "Rarelyused"), ("NUBL", "Neverused Borderline"), ("NU", "Neverused"), ("PU", "PU"), ("U", "Untiered"), ("NA", "n/a")
    ]

    TYPE_LIST = [
        ("normal", "normal"), ("fire", "fire"), ("water", "water"), ("grass", "grass"), ("flying", "flying"), ("fighting", "fighting"), 
        ("poison", "poison"), ("electric", "electric"), ("ground", "ground"), ("rock", "rock"), ("psychic", "psychic"), ("ice", "ice"), 
        ("bug", "bug"), ("ghost", "ghost"), ("steel", "steel"), ("dragon", "dragon"), ("dark", "dark"), ("fairy", "fairy")
    ]

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type_1 = models.CharField(max_length=255, choices=TYPE_LIST)
    type_2 = models.CharField(max_length=255, blank=True, null=True, choices=TYPE_LIST)
    ability_1 = models.ForeignKey(Ability, on_delete=models.PROTECT, related_name="ability_1")
    ability_2 = models.ForeignKey(Ability, null=True, blank=True, on_delete=models.PROTECT, related_name="ability_2")
    ability_3 = models.ForeignKey(Ability, null=True, blank=True, on_delete=models.PROTECT, related_name="ability_3")
    artwork = models.ForeignKey(Art, on_delete=models.CASCADE)
    base_hp = models.IntegerField()
    base_att = models.IntegerField()
    base_def = models.IntegerField()
    base_sp_att = models.IntegerField()
    base_sp_def = models.IntegerField()
    base_spd = models.IntegerField()
    tier = models.CharField(max_length=255, choices=TIER_LIST, null=True, default="U")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ["name"]


class CustomPokemon(models.Model):
    NATURE_LIST = [
        ("ADAMANT","Adamant"), ("MODEST", "Modest")
    ]

    pokemon = models.ForeignKey(BasePokemon, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=55, blank=True, null=True)
    nature = models.CharField(choices=NATURE_LIST, max_length=255, null=True)
    ability = models.ForeignKey(Ability, on_delete=models.PROTECT)
    held_item = models.CharField(max_length=255, null=True, blank=True)
    ivs_hp = models.IntegerField(default=31)
    ivs_att = models.IntegerField(default=31)
    ivs_def = models.IntegerField(default=31)
    ivs_sp_att = models.IntegerField(default=31)
    ivs_sp_def = models.IntegerField(default=31)
    ivs_spd = models.IntegerField(default=31)
    evs_hp = models.IntegerField(default=0)
    evs_att = models.IntegerField(default=0)
    evs_def = models.IntegerField(default=0)
    evs_sp_att = models.IntegerField(default=0)
    evs_sp_def = models.IntegerField(default=0)
    evs_spd = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.pokemon)


class CustomTeam(models.Model):
    creator = models.ForeignKey(Username, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    match_format = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    pk_1 = models.ForeignKey(CustomPokemon, on_delete=models.PROTECT, related_name="pk_1")
    pk_2 = models.ForeignKey(CustomPokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="pk_2")
    pk_3 = models.ForeignKey(CustomPokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="pk_3")
    pk_4 = models.ForeignKey(CustomPokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="pk_4")
    pk_5 = models.ForeignKey(CustomPokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="pk_5")
    pk_6 = models.ForeignKey(CustomPokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="pk_6")


class Battle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    match_format = models.CharField(max_length=255)
    gametype = models.CharField(max_length=255)
    player_1 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="player_1")
    player_2 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="player_2")
    victor = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="victor")
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    teams = models.ManyToManyField(CustomTeam, blank=True, null=True, related_name="matches")
    p1_pk_1 = models.ForeignKey(BasePokemon, on_delete=models.PROTECT, related_name="p1_pk_1")
    p1_pk_2 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p1_pk_2")
    p1_pk_3 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p1_pk_3")
    p1_pk_4 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p1_pk_4")
    p1_pk_5 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p1_pk_5")
    p1_pk_6 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p1_pk_6")
    p2_pk_1 = models.ForeignKey(BasePokemon, on_delete=models.PROTECT, related_name="p2_pk_1")
    p2_pk_2 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p2_pk_2")
    p2_pk_3 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p2_pk_3")
    p2_pk_4 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p2_pk_4")
    p2_pk_5 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p2_pk_5")
    p2_pk_6 = models.ForeignKey(BasePokemon, null=True, blank=True, on_delete=models.PROTECT, related_name="p2_pk_6")

    def __str__(self) -> str:
        return str(self.title)

