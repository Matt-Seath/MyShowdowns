from enum import unique
from django.db import models

# Create your models here.
class Username(models.Model):
    name = models.CharField(max_length=255)
    sprite = models.ImageField(null=True)


class Battle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    match_format = models.CharField(max_length=255)
    player_1 = models.ForeignKey(Username, on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Username, on_delete=models.PROTECT)
    victor = models.ForeignKey(Username, on_delete=models.PROTECT)


class PokemonType(models.Model):
    title = models.CharField(max_length=255)
    sprite = models.ImageField()


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    dex_number = models.IntegerField()
    type_1 = models.ForeignKey(PokemonType, on_delete=models.PROTECT)
    type_2 = models.ForeignKey(PokemonType, null=True, on_delete=models.PROTECT)
    sprite = models.ImageField()
    

