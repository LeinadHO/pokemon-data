import requests
import json

def get_pokemon_data():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/")
    request_json = json.loads(request.content)
    qtd_pokemons = request_json['count']

    pokemons_list = requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit={qtd_pokemons}")
    pokemons_list_json = json.loads(pokemons_list.content)
    print(pokemons_list_json['results'][0]['url'])

    for index_pokemon in range (1, qtd_pokemons):
        pokemon = requests.get(pokemons_list_json['results'][index_pokemon]['url'])
        pokemon_json = json.loads(pokemon.content)
        print(pokemon_json['name'])
        print(index_pokemon)

if __name__ == '__main__':
    get_pokemon_data()

