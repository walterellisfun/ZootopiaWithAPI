import json


def load_data(file_path):
    """Safely load JSON data from a file."""
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_value(data, target_key):
    """Retrieve a value from a dictionary ignoring key capitalization."""
    if not isinstance(data, dict):
        return None

    for key, value in data.items():
        if key.lower() == target_key.lower():
            return value
    return None


def print_attribute(data, key_path, label, index=None):
    """
    Navigate a nested data structure using a dot-path and print the result.

    :param data: Dictionary to traverse.
    :param key_path: Dot-separated path to the value (e.g., "characteristics.diet").
    :param label: Label to print with the value.
    :param index: Optional list index to retrieve.
    """
    value = data

    # Traverse dot-path
    for key in key_path.split('.'):
        value = get_value(value, key)
        if not value:
            return

    # Extract list item safely
    if index is not None:
        if isinstance(value, list) and index < len(value):
            value = value[index]
        else:
            return

    print(f"{label}: {value}")


def print_animal_data(animals_data):
    """Print name, diet, location, and type for each animal."""
    for animal in animals_data:
        print_attribute(animal, "name", "Name")
        print_attribute(animal, "characteristics.diet", "Diet")
        print_attribute(animal, "locations", "Location", index=0)
        print_attribute(animal, "characteristics.type", "Type")
        print()


if __name__ == "__main__":
    animals = load_data('animals_data.json')
    print_animal_data(animals)