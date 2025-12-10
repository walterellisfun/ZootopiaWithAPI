import json


def load_data(file_path):
    """Safely load JSON data from a file."""
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_file(file_path):
    """Read text content from a file."""
    try:
        with open(file_path, "r") as handle:
            return handle.read()
    except FileNotFoundError:
        return ""


def write_file(file_path, content):
    """Write text content to a file."""
    with open(file_path, "w") as handle:
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
    """
    Navigate a nested data structure and return a formatted HTML string.

    :param data: Dictionary to traverse.
    :param key_path: Dot-separated path to the value.
    :param label: Label to print with the value.
    :param index: Optional list index to retrieve.
    :return: Formatted HTML string (e.g., "Label: Value<br/>\n") or empty.
    """
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

    return f"{label}: {value}<br/>\n"


def generate_animals_info(animals):
    """Generate an HTML string containing all animal data."""
    output = ""
    for animal in animals:
        output += '<li class="cards__item">\n'
        output += get_attribute_string(animal, "name", "Name")
        output += get_attribute_string(animal, "characteristics.diet", "Diet")
        output += get_attribute_string(animal, "locations", "Location", index=0)
        output += get_attribute_string(animal, "characteristics.type", "Type")
        output += '</li>\n'
    return output


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    template_content = read_file('animals_template.html')

    animals_info = generate_animals_info(animals_data)
    new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    write_file('animals.html', new_html)