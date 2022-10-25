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

            for i in range(1120, total_count):
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
                        elif response.status_code == 404:
                            print(f"{image} does not exist.")                
                        else:
                            print("Error. Could not retrieve" + image)
                    
                    bar("Retrieving Official Artwork", i, total_count, print_info)


        def get_sprites(pokemon_list, sprite_path, sprite_shiny_path):
            total_count = pokemon_list["count"]

            for i in range(1120, total_count):
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

                    test = requests.get(front_request_url)
                    if test.status_code == 404:
                        # print(f"{pokemon} does not exist.")
                        pass
                        

                    for item in list_of_sprite_tuples:
                        url_request, sprite = item

                        file = open(sprite, "wb")

                        response = requests.get(url_request)
                        if response.status_code == 200:
                            file.write(requests.get(url_request).content)
                            file.close

                            # print(sprite + " has successfully downloaded.")

                        else:
                            # print("Error. Could not retrieve" + sprite)
                            pass

                    bar("Retrieving Default and Shiny Sprites", i , total_count, print_info)
                


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
        url_request = "https://pokeapi.co/api/v2/pokemon/?limit=1000000"
        response = requests.get(url_request)

        if response.status_code == 200:
            pokemon_list = response.json()
            artwork_path, sprite_path, sprite_shiny_path = build_media_directories()
            get_artwork(pokemon_list, artwork_path)
            get_sprites(pokemon_list, sprite_path, sprite_shiny_path)

            print("Done.")