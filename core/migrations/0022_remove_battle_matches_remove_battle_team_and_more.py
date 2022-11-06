# Generated by Django 4.1.2 on 2022-11-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_custompokemon_held_item_customteam_battle_matches_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battle',
            name='matches',
        ),
        migrations.RemoveField(
            model_name='battle',
            name='team',
        ),
        migrations.AddField(
            model_name='battle',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='matches', to='core.customteam'),
        ),
    ]
