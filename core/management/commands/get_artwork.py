from django.core.management.base import BaseCommand
from django.db import connection
from myshowdowns import settings
from pathlib import Path
import requests
import sys
import os


class Command(BaseCommand):
    help = 'Creates Directories within the project and populates them with official pokemon artwork images'

    def handle(self, *args, **options):

        def get_artwork(pokemon_id, artwork_path):
            """Download the artwork for each pokemon and store it in the created directory"""
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


        def build_media_directories():
            """Create directories to store images on the local file system"""
            artwork_path = os.path.join(settings.BASE_DIR, "media/artwork/pokemon/")
            Path(artwork_path).mkdir(parents=True, exist_ok=True)
            
            return artwork_path


        def progress_bar(task, current, total):
            percentage_complete = round((current / total) * 100)
            bar_full = round(percentage_complete / 2)
            full_pixels = "=" * bar_full
            bar_empty = 50 - bar_full
            empty_pixels = " " * bar_empty
            if (current + 1) == total:
                print(f"{task} Completed.")
            else:
                print(f"{task} [{full_pixels}{empty_pixels}] {current} of {total} ({percentage_complete}% Complete.)", end="\r")
                sys.stdout.write("\033[K")


        artwork_path = build_media_directories()

        """Get count and names of current Pokemon"""
        url_request = "https://pokeapi.co/api/v2/pokemon/?limit=1000000"
        response = requests.get(url_request)
        if response.status_code == 200:
            pokemon_list = response.json()
            total_count = pokemon_list["count"]

            # for item in pokemon_list["results"]:
            for i in range(1130, total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    pokemon_name = pokemon["name"]
                    print(pokemon_id + ": " + pokemon_name)

                    get_artwork(pokemon_id, artwork_path)
                    progress_bar("populating the database", i, total_count)
            print("Done.")