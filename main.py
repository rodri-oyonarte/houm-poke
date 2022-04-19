from calls import get_all_pokemon


# funcion para obtener cuantos pokemon tiene at en su nombre y ademas tiene dos a. Retona un numero
def get_pokemon_at():
    # obtener todos los pokemon
    pokemones = get_all_pokemon()
    cadena_buscar = 'at'
    char_buscar = 'a'
    count = 0

    for pokemon in pokemones:
        if pokemon.find(cadena_buscar) > 0:
            lst_aux = []
            for pos,char in enumerate(pokemon):
                if char == char_buscar:
                    lst_aux.append(pos)
            if len(lst_aux) == 2:
                count += 1


    return count


# funcion para conocer con cuantas especies de pokemon puede procrear raichu. Retorna un numero
def raichu_egg():
    pass


# funcion para conocer el peso maximo y minimo de los pokemon de tipo fighting de primera generacion.
# retorna lista [MAX,min]
def cotas_peso_fighting():
    pass

print(get_pokemon_at())