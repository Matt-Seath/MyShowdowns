from django.core.management.base import BaseCommand
from django.db import connection
from myshowdowns import settings
from .progress_bar import bar
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

class Command(BaseCommand):
    help = 'Creates Directories within the project and populates them with official pokemon artwork images'


    def handle(self, *args, **options):    

        TEXT_STRINGS = [
            "|player|p1|", "|player|p2|",
            "|tier|", "|gametype|",
            "|win|", 


        ]

        BATTLE_VARS = [
            "player_1", "player_2",
            "tier", "gametype",
            "victor",
            ""
        ]
        
        battle_dict = {}

        def find_value(string, text, ignore_commas=False):
            start_index = text.find(string)
            start_index += len(string)
            end_index = text.find("|", start_index)
            end_line = text.find("\n", start_index)
            if end_index > end_line:
                end_index = end_line
            if not ignore_commas:
                end_comma = text.find(",", start_index)
                if end_index > end_comma:
                    end_index = end_comma
            string = text[start_index:end_index]

            return string


        url = "https://replay.pokemonshowdown.com/gen8ou-1682017822-nz8a2vmvbbyi2gcmrfbp9u41u4tgjg3pw"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        script = doc.find_all("script")
        if script:
            text = script[1].get_text()
            for i in range(len(TEXT_STRINGS)):
                value = find_value(TEXT_STRINGS[i], text)
                if value:
                    battle_dict[BATTLE_VARS[i]] = value
                else:
                    print(f"Error! Could not find {TEXT_STRINGS[i]}")
                    return 1
            print(battle_dict)
        
        else:
            print("not found")

        # gen = doc.find_all(text="")

        # print(gen)
