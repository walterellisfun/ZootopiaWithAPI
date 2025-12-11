# Zootopia Animal Generator

A Python-based web generator that fetches animal data from the [Ninja API](https://api-ninjas.com/) and generates a static HTML website with the results.

## Features
- Fetches real-time data using the API Ninjas Animals API.
- Generates a responsive HTML card view.
- Handles errors for invalid inputs or empty results.
- Securely manages API keys using environment variables.

## Installation

1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your [API key](https://api-ninjas.com/):
   ```text
   API_KEY='your_api_key_here'
   ```

## Usage

Run the generator script:
```bash
python animals_web_generator.py
```
Enter an animal name (e.g., "Fox") when prompted. The script will generate an `animals.html` file in the same directory.