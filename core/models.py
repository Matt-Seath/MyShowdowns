from django.db import models


# Create your models here.
class Sprite(models.Model):
    front = models.ImageField()
    front_shiny = models.ImageField()
    back = models.ImageField()
    back_shiny = models.ImageField()


class Ability(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True)


class Username(models.Model):
    name = models.CharField(max_length=255)
    sprite = models.ForeignKey(Sprite, null=True, blank=True, on_delete=models.PROTECT)


class Battle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    match_format = models.CharField(max_length=255)
    player_1 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="player_1")
    player_2 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="player_2")
    victor = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="victor")
    description = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now=True)


class PokemonType(models.Model):
    title = models.CharField(max_length=255)
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)


class BasePokemon(models.Model):
    TIER_LIST = [
        ("UBER", "Uber"), ("OU", "Overused"), ("UUBL", "Underused Borderline"), ("UU", "Underused"), ("RUBL", "Rarelyused Borderline"),
        ("RU", "Rarelyused"), ("NUBL", "Neverused Borderline"), ("NU", "Neverused"), ("PU", "PU"), ("U", "Untiered"), ("NA", "n/a")
    ]

    name = models.CharField(max_length=255)
    dex_number = models.IntegerField()
    type_1 = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name="type_1")
    type_2 = models.ForeignKey(PokemonType, null=True, on_delete=models.PROTECT, related_name="type_2")
    ability_1 = models.ForeignKey(Ability, on_delete=models.PROTECT, related_name="ability_1")
    ability_2 = models.ForeignKey(Ability, on_delete=models.PROTECT, related_name="ability_2")
    ability_3 = models.ForeignKey(Ability, on_delete=models.PROTECT, related_name="ability_3")
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)
    base_hp = models.IntegerField()
    base_att = models.IntegerField()
    base_def = models.IntegerField()
    base_sp_att = models.IntegerField()
    base_sp_def = models.IntegerField()
    base_spd = models.IntegerField()
    tier = models.CharField(max_length=255, choices=TIER_LIST, default="NA")


class CustomPokemon(models.Model):
    NATURE_LIST = [
        ("ADAMANT","Adamant"), ("MODEST", "Modest")
    ]

    pokemon = models.ForeignKey(BasePokemon, on_delete=models.CASCADE)
    nature = models.CharField(choices=NATURE_LIST, max_length=255, null=True)
    ability = models.ForeignKey(Ability, on_delete=models.PROTECT)
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



