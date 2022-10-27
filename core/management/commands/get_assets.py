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
                            print(image + " has successfully downloaded.")
                        elif artwork_response.status_code == 404:
                            print(f"{image} does not exist.")                
                        else:
                            print("Error. Could not retrieve" + image)
                    
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
                    if "effect_entries" in ability:
                        if len(ability["flavor_text_entries"]) > 7:
                            ability_effect = ability["flavor_text_entries"][7]["flavor_text"]             
                        elif len(ability["effect_entries"]) == 2:
                            ability_effect = ability["effect_entries"][1]["effect"]
                        elif len(ability["effect_entries"]) == 1:
                            ability_effect = ability["effect_entries"][0]["effect"]
                        elif len(ability["effect_entries"]) == 0:
                                ability_effect = "Data not found."
                    info = f"{ability_id}: {ability_name}"

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
                            ability_1 = pokemon["abilities"][0]["ability"]["name"]
                        else:
                            ability_1 = None
                        if ability_count > 1:
                            ability_2 = pokemon["abilities"][1]["ability"]["name"]
                        else:
                            ability_2 = None
                        if ability_count > 2:
                            ability_3 = pokemon["abilities"][2]["ability"]["name"]
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

                    # with connection.cursor() as cursor:
                    #     cursor.execute(
                    #         """INSERT INTO core_basepokemon (
                    #             name, type_1, type_2, ability_1, ability_2, ability_3, 
                    #             artwork, base_hp, base_att, base_def, base_sp_att, base_sp_def, base_spd)
                    #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                    #             (
                    #                 name, type_1, type_2, ability_1, ability_2, ability_3, 
                    #                 artwork, base_hp, base_att, base_def, base_sp_att, base_sp_def, base_spd
                    #             )
                    #     )

                    bar("Populating Ability Table", i, total_count, info)


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

            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    
                    artwork = artwork_path + pokemon_id + ".png"
                    artwork_image_path = Path(artwork)
                    if artwork_image_path.exists():        
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO core_art (artwork) VALUES (%s)", (artwork, ))

                    sprite = sprite_path + pokemon_id + ".png"
                    sprite_image_path = Path(sprite)
                    if sprite_image_path.exists():        
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO core_art (front) VALUES (%s)", (sprite, ))

                    sprite_shiny = sprite_shiny_path + pokemon_id + ".png"
                    shiny_image_path = Path(sprite_shiny)
                    if shiny_image_path.exists():        
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO core_art (front_shiny) VALUES (%s)", (sprite_shiny, ))

                    bar("Populating Ability Table", i, total_count)


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
            # populate_pokemon_type_table()
            # get_artwork(pokemon_list, artwork_path)
            # get_sprites(pokemon_list, sprite_path, sprite_shiny_path)
            populate_artwork_table(pokemon_list, artwork_path, sprite_path, sprite_shiny_path)
            # populate_pokemon_table(pokemon_list)
            # populate_ability_table(ability_list)

            print(" ")
            print("Done.")