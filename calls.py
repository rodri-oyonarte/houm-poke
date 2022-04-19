import json
import requests


# funcion para obtener todos los pokemon existentes
def get_all_pokemon():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1126")
    resp = json.loads(request.text)

    poke_list = []

    for pokemon in resp['results']:
        poke_list.append(pokemon['name'])

    return poke_list


# funcion para obtener los egg group de una especie
def get_egg_group_especie(especie):
    request = requests.get("https://pokeapi.co/api/v2/pokemon-species/{}/".format(especie))
    resp = json.loads(request.text)
    egg_group = resp['egg_groups']

    return egg_group


# funcion para obtener los pokemon de un mismo egg group
def get_pokemon_por_egg_group(egg_group):
    request = requests.get(egg_group['url'])
    resp = json.loads(request.text)
    pokemones_egg = []

    for pokemon in resp['pokemon_species']:
        pokemones_egg.append(pokemon['name'])

    return pokemones_egg


# funcion para obtener pokemones por tipo
def get_pokemon_por_tipo(tipo):
    request = requests.get("https://pokeapi.co/api/v2/type/2/".format(tipo))
    resp = json.loads(request.text)
    pokemones_lucha = resp['pokemon']

    return pokemones_lucha


# funcion para obtener un pokemon
def get_pokemon(url):
    request = requests.get(url)
    pokemon = json.loads(request.text)

    return pokemon



