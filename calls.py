import json
import requests


# funcion para obtener todos los pokemon existentes
def get_all_pokemon():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1126")
    text = json.loads(request.text)

    poke_list = []

    for pokemon in text['results']:
        poke_list.append(pokemon['name'])

    return poke_list


# funcion para obtener los egg group de una especie
def get_egg_group_especie(especie):
    request = requests.get("https://pokeapi.co/api/v2/pokemon-species/{}/".format(especie))
    text = json.loads(request.text)
    egg_group = text['egg_groups']

    return egg_group


# funcion para obtener los pokemon de un mismo egg group
def get_pokemon_por_egg_group(egg_group):
    request = requests.get(egg_group['url'])
    text = json.loads(request.text)
    pokemones_egg = []

    for pokemon in text['pokemon_species']:
        pokemones_egg.append(pokemon['name'])

    return pokemones_egg


# funcion para obtener pokemones por tipo
def get_pokemon_por_tipo():
    return 0


# funcion para obtener un pokemon
def get_pokemon(name):
    pokemon = 0
    return pokemon



