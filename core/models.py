from django.db import models


# Create your models here.
class Sprite(models.Model):
    image = models.ImageField()


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
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)


class PokemonType(models.Model):
    title = models.CharField(max_length=255)
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)


class BasePokemon(models.Model):
    TIER_LIST = [
        "UBER", "OU", "UUBL", "UU", "RUBL",
        "RU", "NUBL", "NU", "PU", "UNTIERED", "NA"
    ]

    name = models.CharField(max_length=255)
    dex_number = models.IntegerField()
    type_1 = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name="type_1")
    type_2 = models.ForeignKey(PokemonType, null=True, on_delete=models.PROTECT, related_name="type_2")
    ability_1 = models.CharField(max_length=255, null=True)
    ability_2 = models.CharField(max_length=255, null=True)
    ability_3 = models.CharField(max_length=255, null=True)
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)
    base_hp = models.IntegerField()
    base_att = models.IntegerField()
    base_def = models.IntegerField()
    base_sp_att = models.IntegerField()
    base_sp_def = models.IntegerField()
    base_spd = models.IntegerField()
    tier = models.CharField(max_length=255, choices=TIER_LIST, default="NA")


class CustomPokemon(models.Model):
    pokemon = models.ForeignKey(BasePokemon, on_delete=models.CASCADE)
    ivs_hp = models.IntegerField(default=31)
    ivs_att = models.IntegerField(default=31)
    ivs_def = models.IntegerField(default=31)
    ivs_sp_att = models.IntegerField(default=31)
    ivs_sp_def = models.IntegerField(default=31)
    ivs_spd = models.IntegerField(default=31)

    

