# Generated by Django 4.1.2 on 2022-10-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_basepokemon_ability_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepokemon',
            name='tier',
            field=models.CharField(choices=[('UBER', 'Uber'), ('OU', 'Overused'), ('UUBL', 'Underused Borderline'), ('UU', 'Underused'), ('RUBL', 'Rarelyused Borderline'), ('RU', 'Rarelyused'), ('NUBL', 'Neverused Borderline'), ('NU', 'Neverused'), ('PU', 'PU'), ('U', 'Untiered'), ('NA', 'n/a')], max_length=255, null=True),
        ),
    ]
