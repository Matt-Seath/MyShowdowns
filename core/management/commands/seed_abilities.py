from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import requests



class Command(BaseCommand):
    help = 'Populates the database with pokemon abilities'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM core_ability")

        for ability in range(1000):
            ability = str(ability + 1)
            print(ability)
            url_request = f"https://pokeapi.co/api/v2/ability/{ability}"
            response = requests.get(url_request)

            if response.status_code == 200:
                ability = response.json()
                if "id" in ability:
                    ability_id = ability["id"]
                if "name" in ability:
                    ability_name = ability["name"]
                    print(ability_name)
                if "effect_entries" in ability:
                    if len(ability["effect_entries"]) == 2:
                        ability_effect = ability["effect_entries"][1]["effect"]
                    elif len(ability["effect_entries"]) == 1:
                        ability_effect = ability["effect_entries"][0]["effect"]
                    elif len(ability["effect_entries"]) == 0:
                        if len(ability["flavor_text_entries"]) > 7:
                            ability_effect = ability["flavor_text_entries"][7]["flavor_text"]             
                        else:
                            ability_effect = "Data not found."
                
                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO core_ability (id, name, effect)
                        VALUES (%s, %s, %s)""", (ability_id, ability_name, ability_effect)
                    )
                print("Successfully added " + ability_name + " to the database.")

            elif response.status_code == 404:
                print(f"{ability} does not exist.")
                break

            else:
                print(f"Error: Status = {response.status_code}. Data not found")

        print("Done.")

