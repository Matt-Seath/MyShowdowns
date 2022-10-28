from django.core.management.base import BaseCommand
from django.db import connection
from myshowdowns import settings
from .progress_bar import bar
from pathlib import Path
import requests
import os


class Command(BaseCommand):
    help = 'Creates Directories within the project and populates them with official pokemon artwork images'

    def handle(self, *args, **options):

        def get_artwork(pokemon_list, artwork_path):
            """Download the artwork for each pokemon and store it in the created directory"""
            total_count = pokemon_list["count"]

            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    pokemon_name = pokemon["name"]
                    print_info = (pokemon_id + ": " + pokemon_name)

                    artwork_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
                    image = artwork_path + pokemon_id + ".png"
                    image_path = Path(image)

                    if not image_path.exists():      
                        artwork_response = requests.get(artwork_url)
                        if artwork_response.status_code == 200:
                            file = open(image, "wb")
                            file.write(artwork_response.content)
                            file.close
                    
                    bar("Retrieving Official Artwork", i, total_count, print_info)


        def get_sprites(pokemon_list, sprite_path, sprite_shiny_path):
            total_count = pokemon_list["count"]

            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    pokemon_name = pokemon["name"]
                    print_info = (pokemon_id + ": " + pokemon_name)

                    front_sprite = sprite_path + pokemon_id + ".png"
                    front_shiny_sprite = sprite_shiny_path + pokemon_id + ".png"  
                    front_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
                    front_shiny_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{pokemon_id}.png"

                    list_of_sprite_tuples = [
                        (front_request_url, front_sprite), (front_shiny_request_url, front_shiny_sprite), 
                    ]

                    for item in list_of_sprite_tuples:
                        url_request, sprite = item

                        file = open(sprite, "wb")

                        response = requests.get(url_request)
                        if response.status_code == 200:
                            file.write(requests.get(url_request).content)
                            file.close

                    bar("Retrieving Default and Shiny Sprites", i , total_count, print_info)
                

        def populate_ability_table(ability_list):
            total_count = ability_list["count"]

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM core_ability")

            for i in range(total_count):
                list_item = ability_list["results"][i]
                ability = list_item["name"]
                url_request = f"https://pokeapi.co/api/v2/ability/{ability}"
                response = requests.get(url_request)

                if response.status_code == 200:
                    ability = response.json()
                    if "id" in ability:
                        ability_id = ability["id"]
                    if "name" in ability:
                        ability_name = ability["name"]
                    if "flavor_text_entries" in ability:
                        entry_count = len(ability["flavor_text_entries"])
                        for entry in range(entry_count):
                            valid_entry = ability["flavor_text_entries"][entry]["flavor_text"]  
                            entry_lang = ability["flavor_text_entries"][entry]["language"]["name"]
                            if valid_entry and entry_lang == "en":
                                ability_effect = valid_entry
                                break

                    info = f"{ability_id}: {ability_name}"

                    if ability_id < 1000:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                """INSERT INTO core_ability (id, name, effect)
                                VALUES (%s, %s, %s)""", (ability_id, ability_name, ability_effect)
                            )
                         # print("Successfully added " + ability_name + " to the database.")

                    bar("Populating Ability Table", i, total_count, info)


        def populate_pokemon_table(pokemon_list):
            total_count = pokemon_list["count"]
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM core_basepokemon")

            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_name = list_item["name"]
                url_request = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
                response = requests.get(url_request)

                if response.status_code == 200:
                    pokemon = response.json()
                    if "id" in pokemon:
                        pokemon_id = pokemon["id"]
                    if "name" in pokemon:
                        name = pokemon["name"]
                    if "abilities" in pokemon:
                        ability_count = len(pokemon["abilities"])
                        if ability_count > 0:
                            # ability_1 = pokemon["abilities"][0]["ability"]["name"]
                            ability_1 = int(pokemon["abilities"][0]["ability"]["url"].rsplit('/', )[-2])
                        else:
                            ability_1 = None
                        if ability_count > 1:
                            # ability_2 = pokemon["abilities"][1]["ability"]["name"]
                            ability_2 = int(pokemon["abilities"][1]["ability"]["url"].rsplit('/', )[-2])
                        else:
                            ability_2 = None
                        if ability_count > 2:
                            # ability_3 = pokemon["abilities"][2]["ability"]["name"]
                            ability_3 = int(pokemon["abilities"][2]["ability"]["url"].rsplit('/', )[-2])
                        else:
                            ability_3 = None
                    if "types" in pokemon:
                        type_count = len(pokemon["types"])
                        type_1 = pokemon["types"][0]["type"]["name"]
                        if type_count == 2:
                            type_2 = pokemon["types"][1]["type"]["name"]
                        else:
                            type_2 = None
                    if "stats" in pokemon:
                        base_hp = (pokemon["stats"][0]["base_stat"])
                        base_att = (pokemon["stats"][1]["base_stat"])
                        base_def = (pokemon["stats"][2]["base_stat"])
                        base_sp_att = (pokemon["stats"][3]["base_stat"])
                        base_sp_def = (pokemon["stats"][4]["base_stat"])
                        base_spd = (pokemon["stats"][5]["base_stat"])

                    info = f"{pokemon_id}: {name}"

                    with connection.cursor() as cursor:
                        cursor.execute(
                            """INSERT INTO core_basepokemon (
                                id, name, type_1, type_2, ability_1_id, ability_2_id, ability_3_id, 
                                artwork_id, base_hp, base_att, base_def, base_sp_att, base_sp_def, base_spd)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                                (
                                    pokemon_id, name, type_1, type_2, ability_1, ability_2, ability_3, 
                                    pokemon_id, base_hp, base_att, base_def, base_sp_att, base_sp_def, base_spd
                                )
                        )

                    bar("Populating Pokemon Table", i, total_count, info)


        def populate_pokemon_type_table():
            type_list = [
                "normal", "fire", "Water", "Grass", "Flying", "Fighting", 
                "Poison", "Electric", "Ground", "Rock", "Psychic", "Ice", 
                "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"
            ]
    
            for i in range(len(type_list)):
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """INSERT INTO core_pokemontype (name)
                            VALUES (%s)""", (type_list[i],)
                        )

                    bar("Populating PokemonType Table", i, len(type_list))


        def populate_artwork_table(pokemon_list, artwork_path, sprite_path, sprite_shiny_path):
            total_count = pokemon_list["count"]
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM core_art")

            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    name = pokemon["name"]
                    info = f"{pokemon_id}: {name}"

                    
                    artwork = artwork_path + pokemon_id + ".png"
                    artwork_image_path = Path(artwork)
                    if not artwork_image_path.exists():        
                        artwork = None
                    sprite = sprite_path + pokemon_id + ".png"
                    sprite_image_path = Path(sprite)
                    if not sprite_image_path.exists():        
                        sprite = None
                    sprite_shiny = sprite_shiny_path + pokemon_id + ".png"
                    shiny_image_path = Path(sprite_shiny)
                    if not shiny_image_path.exists():  
                        sprite_shiny = None      
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO core_art (id, artwork, front, front_shiny) VALUES (%s, %s, %s, %s)", 
                            (pokemon["id"], artwork, sprite, sprite_shiny))

                    bar("Populating Artwork Table", i, total_count, info)


        def build_media_directories():
            """Create directories to store images on the local file system"""
            artwork_path = os.path.join(settings.BASE_DIR, "media/artwork/pokemon/")
            sprite_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/default/")
            sprite_shiny_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/shiny/")

            dirs_to_make = [
                artwork_path, sprite_path, sprite_shiny_path,
            ]
            for new_dir in dirs_to_make:
                Path(new_dir).mkdir(parents=True, exist_ok=True)
            
            return artwork_path, sprite_path, sprite_shiny_path


       


        """Get count and names of current Pokemon"""
        pokemon_request = "https://pokeapi.co/api/v2/pokemon/?limit=1000000"
        ability_request = "https://pokeapi.co/api/v2/ability/?limit=1000000"
        pokemon_response = requests.get(pokemon_request)
        ability_response = requests.get(ability_request)


        if pokemon_response.status_code == 200 and ability_response.status_code == 200:
            print("Retrieving Assets...")
            print(" ")

            pokemon_list = pokemon_response.json()
            ability_list = ability_response.json()
            artwork_path, sprite_path, sprite_shiny_path = build_media_directories()
            populate_pokemon_type_table()
            get_artwork(pokemon_list, artwork_path)
            get_sprites(pokemon_list, sprite_path, sprite_shiny_path)
            populate_artwork_table(pokemon_list, artwork_path, sprite_path, sprite_shiny_path)
            populate_ability_table(ability_list)
            populate_pokemon_table(pokemon_list)

            print(" ")
            print("Done.")