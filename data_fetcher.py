import requests

API_KEY = 'k3cuX8inqk9Hp7kXnkF8lA==mDvFicylQlqc27WO'

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