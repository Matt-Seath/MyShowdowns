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


        """Download the artwork for each pokemon and store it in the created directory"""
        for pokemon in range(5000):
            pokemon = str(pokemon + 1)
            print(pokemon)

            image = artwork_path + pokemon + ".png"

            url_request = f"https://raw.githubusercontent.com/pokeapi/sprites/master/sprites/pokemon/other/official-artwork/{pokemon}.png"


            file = open(image, "wb")

            response = requests.get(url_request)
            if response.status_code == 200:
                file.write(requests.get(url_request).content)
                file.close

                print(image + " has successfully downloaded.")

            elif response.status_code == 404:
                print(f"{image} does not exist.")
                break
             
            else:
                print("Error. Could not retrieve" + image)


        print("Done.")