import requests


def poke_request():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

    if response.status_code == 200:
        payload = response.json()

    return payload
