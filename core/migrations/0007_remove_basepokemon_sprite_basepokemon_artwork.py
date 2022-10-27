# Generated by Django 4.1.2 on 2022-10-27 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_title_pokemontype_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basepokemon',
            name='sprite',
        ),
        migrations.AddField(
            model_name='basepokemon',
            name='artwork',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.art'),
            preserve_default=False,
        ),
    ]