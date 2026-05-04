import os

DB_PATH = "data/database/pokemon.db"
URL_PATH = "https://pokeapi.co/api/v2/"
POKEMON_INPUT = os.getenv("POKEMON_INPUT", "pikachu,charizard,venusaur")
TYPE_INPUT = os.getenv("TYPE_INPUT", "electric")