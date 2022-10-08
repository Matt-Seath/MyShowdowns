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


class PokemonType(models.Model):
    title = models.CharField(max_length=255)
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    dex_number = models.IntegerField()
    type_1 = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name="type_1")
    type_2 = models.ForeignKey(PokemonType, null=True, on_delete=models.PROTECT, related_name="type_2")
    sprite = models.ForeignKey(Sprite, on_delete=models.PROTECT)
    

