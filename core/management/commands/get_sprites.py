from django.core.management.base import BaseCommand
from django.db import connection
from myshowdowns import settings
from pathlib import Path
import requests
import os

NUMBER_OF_POKEMON = 905

class Command(BaseCommand):
    help = 'Creates Directories within the project and populates them with sprite images'

    def handle(self, *args, **options):

        """Create directories to store images on the local file system"""
        front_dir_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/front/")
        front_shiny_dir_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/front_shiny/")
        back_dir_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/back/")
        back_shiny_dir_path = os.path.join(settings.BASE_DIR, "media/sprites/pokemon/back_shiny/")

        list_of_new_dirs = [
            front_dir_path, front_shiny_dir_path, back_dir_path, back_shiny_dir_path,
        ]

        for new_dir in list_of_new_dirs:
            Path(new_dir).mkdir(parents=True, exist_ok=True)


        """Download the sprites associated with each pokemon and save them in their respective directories"""
        for pokemon in range(NUMBER_OF_POKEMON):
            pokemon = str(pokemon + 1)
            print(pokemon)

            front_sprite = front_dir_path + pokemon + ".png"
            front_shiny_sprite = front_shiny_dir_path + pokemon + ".png"
            back_sprite = back_dir_path + pokemon + ".png"
            back_shiny_sprite = back_shiny_dir_path + pokemon + ".png"

            front_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon}.png"
            front_shiny_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{pokemon}.png"
            back_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{pokemon}.png"
            back_shiny_request_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/{pokemon}.png"

            list_of_sprite_tuples = [
                (front_request_url, front_sprite), (front_shiny_request_url, front_shiny_sprite),
                (back_request_url, back_sprite), (back_shiny_request_url, back_shiny_sprite), 
            ]

            for item in list_of_sprite_tuples:
                url_request, sprite = item

                file = open(sprite, "wb")

                response = requests.get(url_request)
                if response.status_code == 200:
                    file.write(requests.get(url_request).content)
                    file.close

                    print(sprite + " has successfully downloaded.")
                
                else:
                    print("Error. Could not retrieve" + sprite)

        

        # print('Populating the database...')
        # current_dir = os.path.dirname(__file__)
        # file_path = os.path.join(current_dir, 'seed.sql')
        # sql = Path(file_path).read_text()

        # with connection.cursor() as cursor:
        #     cursor.execute(sql)

        print("Done.")

