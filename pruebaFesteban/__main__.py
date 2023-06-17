from pruebaFesteban import poke_request

if __name__ == "__main__":
    pokemon_data = poke_request(1)
    print(pokemon_data["name"])
