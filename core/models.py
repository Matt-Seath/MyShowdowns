from django.db import models

# Create your models here.
class Username(models.Model):
    name = models.CharField(max_length=255)


class Battle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    match_format = models.CharField(max_length=255)
    player_1 = models.ForeignKey(Username, on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Username, on_delete=models.PROTECT)
    victor = models.ForeignKey(Username, on_delete=models.PROTECT)


