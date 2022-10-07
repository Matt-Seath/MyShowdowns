from django.db import models

# Create your models here.
class Username(models.Model):
    name = models.CharField(max_length=255)


class Battle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_lenght=255)
    player_1 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="battles")
    player_2 = models.ForeignKey(Username, on_delete=models.PROTECT, related_name="battles")