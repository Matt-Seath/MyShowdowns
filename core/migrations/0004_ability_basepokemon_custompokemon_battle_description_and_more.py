# Generated by Django 4.1.2 on 2022-10-23 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_battle_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasePokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dex_number', models.IntegerField()),
                ('base_hp', models.IntegerField()),
                ('base_att', models.IntegerField()),
                ('base_def', models.IntegerField()),
                ('base_sp_att', models.IntegerField()),
                ('base_sp_def', models.IntegerField()),
                ('base_spd', models.IntegerField()),
                ('tier', models.CharField(choices=[('UBER', 'Uber'), ('OU', 'Overused'), ('UUBL', 'Underused Borderline'), ('UU', 'Underused'), ('RUBL', 'Rarelyused Borderline'), ('RU', 'Rarelyused'), ('NUBL', 'Neverused Borderline'), ('NU', 'Neverused'), ('PU', 'PU'), ('U', 'Untiered'), ('NA', 'n/a')], default='NA', max_length=255)),
                ('ability_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ability_1', to='core.ability')),
                ('ability_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ability_2', to='core.ability')),
                ('ability_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ability_3', to='core.ability')),
                ('sprite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.sprite')),
                ('type_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_1', to='core.pokemontype')),
                ('type_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type_2', to='core.pokemontype')),
            ],
        ),
        migrations.CreateModel(
            name='CustomPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(choices=[('ADAMANT', 'Adamant'), ('MODEST', 'Modest')], max_length=255, null=True)),
                ('ivs_hp', models.IntegerField(default=31)),
                ('ivs_att', models.IntegerField(default=31)),
                ('ivs_def', models.IntegerField(default=31)),
                ('ivs_sp_att', models.IntegerField(default=31)),
                ('ivs_sp_def', models.IntegerField(default=31)),
                ('ivs_spd', models.IntegerField(default=31)),
                ('evs_hp', models.IntegerField(default=0)),
                ('evs_att', models.IntegerField(default=0)),
                ('evs_def', models.IntegerField(default=0)),
                ('evs_sp_att', models.IntegerField(default=0)),
                ('evs_sp_def', models.IntegerField(default=0)),
                ('evs_spd', models.IntegerField(default=0)),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ability')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.basepokemon')),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Pokemon',
        ),
    ]
