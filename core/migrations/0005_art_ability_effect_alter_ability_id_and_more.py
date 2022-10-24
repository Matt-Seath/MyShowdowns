# Generated by Django 4.1.2 on 2022-10-24 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ability_basepokemon_custompokemon_battle_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.ImageField(null=True, upload_to='')),
                ('front', models.ImageField(null=True, upload_to='')),
                ('front_shiny', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='ability',
            name='effect',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ability',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ability',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='basepokemon',
            name='sprite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.art'),
        ),
        migrations.AlterField(
            model_name='pokemontype',
            name='sprite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.art'),
        ),
        migrations.AlterField(
            model_name='username',
            name='sprite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.art'),
        ),
        migrations.DeleteModel(
            name='Sprite',
        ),
    ]
