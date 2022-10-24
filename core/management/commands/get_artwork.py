from django.core.management.base import BaseCommand
from django.db import connection
from myshowdowns import settings
from pathlib import Path
import requests
import os


class Command(BaseCommand):
    help = 'Creates Directories within the project and populates them with official pokemon artwork images'

    def handle(self, *args, **options):

        """Create directories to store images on the local file system"""
        artwork_path = os.path.join(settings.BASE_DIR, "media/artwork/pokemon/")
        Path(artwork_path).mkdir(parents=True, exist_ok=True)

        """Get count and names of current Pokemon"""
        url_request = "https://pokeapi.co/api/v2/pokemon/?limit=1000000"
        response = requests.get(url_request)
        if response.status_code == 200:
            pokemon_list = response.json()
            total_count = pokemon_list["count"]

            # for item in pokemon_list["results"]:
            for i in range(total_count):
                list_item = pokemon_list["results"][i]
                pokemon_response = requests.get(list_item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    pokemon_id = str(pokemon["id"])
                    print(pokemon_id + ": " + pokemon["name"])

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
                        
        print("Done.")