import requests
import json

def get_pokemons_data(pokemons_list):

    qtd_pokemons = get_pokemons_count()
    all_pokemons_list = get_all_pokemons(qtd_pokemons)

    for index_pokemon in range (0, qtd_pokemons):

        pokemon_dict = {}

        pokemon = requests.get(all_pokemons_list['results'][index_pokemon]['url'])
        pokemon_json = json.loads(pokemon.content)

        pokemon_dict['name'] = get_pokemon_name(pokemon_json)

        pokemon_types_list = get_pokemon_types(pokemon_json)
        pokemon_dict['type_1'] = pokemon_types_list[0]
        pokemon_dict['type_2'] = pokemon_types_list[1]

        pokemon_dict['generation'] = get_pokemon_generation(pokemon_json)

        pokemon_stats_list = get_pokemon_stats(pokemon_json)
        pokemon_dict['hp'] = pokemon_stats_list[0]
        pokemon_dict['attack'] = pokemon_stats_list[1]
        pokemon_dict['defense'] = pokemon_stats_list[2]
        pokemon_dict['special_attack'] = pokemon_stats_list[3]
        pokemon_dict['special_defense'] = pokemon_stats_list[4]
        pokemon_dict['speed'] = pokemon_stats_list[5]

        pokemons_list.append(pokemon_json)

def get_pokemon_stats(pokemon):
    pokemon_stats = []
    pokemon_stats.append(pokemon['stats'][0]['base_stat'])
    pokemon_stats.append(pokemon['stats'][1]['base_stat'])
    pokemon_stats.append(pokemon['stats'][2]['base_stat'])
    pokemon_stats.append(pokemon['stats'][3]['base_stat'])
    pokemon_stats.append(pokemon['stats'][4]['base_stat'])
    pokemon_stats.append(pokemon['stats'][5]['base_stat'])
    return pokemon_stats

def get_pokemon_types(pokemon):
    pokemon_types = []
    type1 = pokemon['types'][0]['type']['name']
    pokemon_types.append(type1)
    try:
        type2 = pokemon['types'][1]['type']['name']
    except IndexError:
        type2 = None
    pokemon_types.append(type2)
    return pokemon_types


def get_pokemon_name(pokemon):
    return pokemon['name']

def get_all_pokemons(qtd_pokemons):
    all_pokemons = requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit={qtd_pokemons}")
    all_pokemons_json = json.loads(all_pokemons.content)
    return all_pokemons_json

def get_pokemons_count():
    pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/")
    pokemons_json = json.loads(pokemons.content)
    return pokemons_json['count']

def get_pokemon_generation(pokemon):
    pokemon_species = requests.get(pokemon['species']['url'])
    pokemon_species_json = json.loads(pokemon_species.content)
    return pokemon_species_json['generation']['name']