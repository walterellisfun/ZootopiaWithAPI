import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the key securely
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    api_url = 'https://api.api-ninjas.com/v1/animals'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(api_url, headers=headers, params={'name': animal_name})

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []