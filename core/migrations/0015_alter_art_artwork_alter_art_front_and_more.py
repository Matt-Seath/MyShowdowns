# Generated by Django 4.1.2 on 2022-10-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_custompokemon_nickname_alter_basepokemon_ability_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artwork',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='art',
            name='front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='art',
            name='front_shiny',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='battle',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='custompokemon',
            name='nickname',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
