import requests


def poke_request(id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response.status_code == 200:
        payload = response.json()

    return payload
