import requests


def get_animals_data(name):
    """Fetches animals data from the API."""
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    headers = {'X-Api-Key': 'k3cuX8inqk9Hp7kXnkF8lA==mDvFicylQlqc27WO'}

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []


def read_file(file_path):
    """Read text content from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        return ""


def write_file(file_path, content):
    """Write text content to a file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def get_value(data, target_key):
    """Retrieve a value from a dictionary ignoring key capitalization."""
    if not isinstance(data, dict):
        return None

    for key, value in data.items():
        if key.lower() == target_key.lower():
            return value
    return None


def get_attribute_string(data, key_path, label, index=None):
    """Navigate a nested data structure and return a formatted HTML string."""
    value = data

    # Traverse dot-path
    for key in key_path.split('.'):
        value = get_value(value, key)
        if not value:
            return ""

    # Extract list item safely
    if index is not None:
        if isinstance(value, list) and index < len(value):
            value = value[index]
        else:
            return ""

    return f"<strong>{label}:</strong> {value}<br/>\n"


def serialize_animal(animal_obj):
    """Serialize a single animal object to an HTML list item."""
    output = '<li class="cards__item">\n'

    # 1. Handle Name (Title)
    name = get_value(animal_obj, "name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    # 2. Handle Details (Text Body)
    output += '  <p class="card__text">\n'
    output += get_attribute_string(animal_obj, "characteristics.diet", "Diet")
    output += get_attribute_string(animal_obj, "locations", "Location", index=0)
    output += get_attribute_string(animal_obj, "characteristics.type", "Type")
    output += '  </p>\n'

    output += '</li>\n'
    return output


def generate_animals_info(animals):
    """Generate an HTML string containing all animal data."""
    output = ""
    for animal_obj in animals:
        output += serialize_animal(animal_obj)
    return output


if __name__ == "__main__":
    # Milestone 1: Hardcoded "Fox" search
    animal_name = "Fox"
    animals_data = get_animals_data(animal_name)

    template_content = read_file('animals_template.html')

    # Force the HTML to include the charset definition
    if '<head>' in template_content:
        template_content = template_content.replace('<head>', '<head>\n<meta charset="utf-8">')

    animals_info = generate_animals_info(animals_data)
    print(animals_info)
    new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    write_file('animals.html', new_html)
    print(f"Website generated for '{animal_name}'!")