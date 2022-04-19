from calls import get_all_pokemon, get_egg_group_especie, get_pokemon_por_egg_group


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
    pokemon_egg_group = []
    aux = []
    # obtener los egg_group
    egg_groups = get_egg_group_especie(especie_a_buscar)
    # junto todos en una lista
    for egg_group in egg_groups:
        aux.extend(get_pokemon_por_egg_group(egg_group))
    print(len(aux))

    # elimino los duplicados
    pokemon_egg_group = list(set(aux))

    return pokemon_egg_group


# funcion para conocer el peso maximo y minimo de los pokemon de tipo fighting de primera generacion.
# retorna lista [MAX,min]
def cotas_peso_fighting():
    pass


print(raichu_egg())
