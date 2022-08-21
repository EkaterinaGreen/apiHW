import json
import requests


def max_hero_int():
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    for hero in heroes_list:
        url = f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}'
        hero_dict = json.loads(requests.get(url).content)
        intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

    print("Самым высоким интеллектом обладает супергерой", max(intelligence_dict))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_hero_int()
