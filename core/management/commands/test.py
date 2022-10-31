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
        url = "https://replay.pokemonshowdown.com/gen8ou-1682017822-nz8a2vmvbbyi2gcmrfbp9u41u4tgjg3pw"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        script = doc.find_all(text="script")
        if script:
            print(script)
        else:
            print("not found")

        # gen = doc.find_all(text="")

        # print(gen)
