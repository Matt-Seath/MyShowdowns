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

            for item in pokemon_list["results"]:
                pokemon_response = requests.get(item["url"])
                if pokemon_response.status_code == 200:
                    pokemon = pokemon_response.json()
                    print(pokemon["name"])

                    """Download the artwork for each pokemon and store it in the created directory"""
                    artwork_url = pokemon["sprites"]["other"]["official-artwork"]["front_default"]
                    image = artwork_path + str(pokemon["id"]) + ".png"
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