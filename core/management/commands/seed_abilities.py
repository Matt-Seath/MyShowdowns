from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import requests


NUMBER_OF_ABILITIES = 267

class Command(BaseCommand):
    help = 'Populates the database with pokemon abilities'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM core_ability")

        for ability in range(NUMBER_OF_ABILITIES):
            ability = str(ability + 1)
            print(ability)
            url_request = f"https://pokeapi.co/api/v2/ability/{ability}"
            response = requests.get(url_request)

            if response.status_code == 200:
                ability = response.json()
                ability_id = ability["id"]
                ability_name = ability["name"]
                try:
                    ability_effect = ability["effect_entries"][1]["effect"]
                except:
                    try:
                        ability_effect = ability["effect_entries"][0]["effect"]
                    except:
                        ability_effect = "Data not found."
                
                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO core_ability (id, name, effect)
                        VALUES (%s, %s, %s)""", (ability_id, ability_name, ability_effect)
                    )
                print("Successfully added " + ability_name + " to the database.")
            else:
                print("Error, could not retrive " + ability)

        print("Done.")

