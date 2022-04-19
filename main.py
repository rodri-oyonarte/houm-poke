from urllib import parse
from calls import get_all_pokemon, get_egg_group_especie, get_pokemon_por_egg_group, get_pokemon_por_tipo, get_pokemon


# funcion para obtener cuantos pokemon tiene at en su nombre y ademas tiene dos a. Retona un numero
def get_pokemon_at():
    # obtener todos los pokemon
    pokemones = get_all_pokemon()
    cadena_buscar = 'at'
    char_buscar = 'a'
    count = 0

    for pokemon in pokemones:
        # buscar los poquemones que tienen la cadena 'at'
        if pokemon.find(cadena_buscar) > 0:
            lst_aux = []
            # contar la cantidad de a que hay en el nombre del pokemon
            for pos, char in enumerate(pokemon):
                if char == char_buscar:
                    lst_aux.append(pos)
            if len(lst_aux) == 2:
                count += 1

    return count


# funcion para conocer con cuantas especies de pokemon puede procrear raichu. Retorna un numero
def raichu_egg():
    especie_a_buscar = "raichu"
    
    aux = []
    # obtener los egg_group
    egg_groups = get_egg_group_especie(especie_a_buscar)
    # junto todos en una lista
    for egg_group in egg_groups:
        aux.extend(get_pokemon_por_egg_group(egg_group))

    # elimino los duplicados
    pokemon_egg_group = list(set(aux))

    return len(pokemon_egg_group)


# funcion para conocer el peso maximo y minimo de los pokemon de tipo fighting de primera generacion.
# retorna lista [MAX,min]
def cotas_peso_fighting():
    peso_max = 0
    peso_min = 0

    # obtengo todos los pokemon de tipo lucha
    pokemon_lucha = get_pokemon_por_tipo(2)
    for pokemon_raw in pokemon_lucha:

        # obtengo la info de cada pokemon solo si el id esta entre 1 y 151
        query = parse.urlsplit(pokemon_raw['pokemon']['url'])  # parseo la url para sacar el path
        id_pokemon = int(query.path.split('/')[4])  # busco el id en el path

        if id_pokemon <= 151:
            pokemon = get_pokemon(pokemon_raw['pokemon']['url'])

            # compruebo el peso minimo y maximo de cada pokemon para buscar el mayor
            if peso_max < pokemon['weight']:
                peso_max = (pokemon['weight'])
            if peso_min == 0 or peso_min > pokemon['weight']:
                peso_min = pokemon['weight']

    cota_peso = [peso_max, peso_min]
    return cota_peso
