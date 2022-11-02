# Generated by Django 4.1.2 on 2022-10-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_basepokemon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepokemon',
            name='tier',
            field=models.CharField(choices=[('UBER', 'Uber'), ('OU', 'Overused'), ('UUBL', 'Underused Borderline'), ('UU', 'Underused'), ('RUBL', 'Rarelyused Borderline'), ('RU', 'Rarelyused'), ('NUBL', 'Neverused Borderline'), ('NU', 'Neverused'), ('PU', 'PU'), ('Untiered', 'Untiered'), ('NA', 'n/a')], default='Untiered', max_length=255),
        ),
    ]