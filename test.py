from django.db import connection
from bs4 import BeautifulSoup
import requests


def main(url, description=None):
    TEXT_STRINGS = [
        "|player|p1|", "|player|p2|",
        "|tier|", "|gametype|",
        "|win|",
    ]

    TEXT_PKM = [
        "|poke|p1|", "|poke|p2|",
    ]

    BATTLE_VARS = [
        "player_1", "player_2",
        "match_format", "gametype",
        "victor",
    ]

    BATTLE_PKM = [[
        "p1_pk_1", "p1_pk_2",
        "p1_pk_3", "p1_pk_4",
        "p1_pk_5", "p1_pk_6",
        ], [
        "p2_pk_1", "p2_pk_2",
        "p2_pk_3", "p2_pk_4",
        "p2_pk_5", "p2_pk_6",
    ]]

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
            if end_index > end_comma and end_comma != -1:
                end_index = end_comma
        string = text[start_index:end_index]

        return string


    def find_all(sub, a_str):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            string_end = start + len(sub)
            end_index = a_str.find("|", string_end)
            end_comma = a_str.find(",", string_end)
            if end_index > end_comma and end_comma != -1:
                end_index = end_comma
            yield text[string_end:end_index].lower()
            start += len(sub) # use start += 1 to find overlapping matches
 

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    script = doc.find_all("script")
    if script:
        default_description = doc.find_all("meta")[1].get("content")
        text = script[1].get_text()
        battle_dict["title"] = doc.title.string
        if description:
            battle_dict["description"] = description
        else:
            battle_dict["description"] = default_description
        battle_dict["link"] = url

        for i in range(len(TEXT_STRINGS)):
            value = find_value(TEXT_STRINGS[i], text)
            if value:
                battle_dict[BATTLE_VARS[i]] = value
            else:
                print(f"Error! Could not find {TEXT_STRINGS[i]}")
                return 1
        for i in range(2):
            for j, value in enumerate(find_all(TEXT_PKM[i], text)):
                battle_dict[BATTLE_PKM[i][j]] = value

        print(battle_dict)
    else:
        print("not found")



if __name__ == "__main__":
    main("https://replay.pokemonshowdown.com/gen8ou-1668639742")