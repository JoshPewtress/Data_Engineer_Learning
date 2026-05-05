import logging
import requests

from config import URL_PATH

logger = logging.getLogger(__name__)

def get_pokemon_input():
    while True:
        user_input = input("Enter Pokémon names separated by commas: ")
        pokemon_names = [name.strip().lower() for name in user_input.split(",") if name.strip()]
        
        if pokemon_names:
            return pokemon_names
        
        print("No valid Pokémon names entered.")

def extract(pokemon_names):
    output = []
    max_retries = 3

    for name in pokemon_names:
        name = name.strip().lower().replace(" ", "-")
        
        if not name:
            continue

        success = False

        for attempt in range(max_retries):
            try:    
                url = f"{URL_PATH}pokemon/{name}"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    output.append(response.json())
                    success = True
                    break

                logger.warning(f"Attempt {attempt + 1} failed for {name}: {response.status_code}")

            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed for {name}: {e}")

        if not success:
            logger.error(f"Skipping {name}: failed after {max_retries} attempts")
    
    return output