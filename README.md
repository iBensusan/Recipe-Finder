# Recipe Finder

A Python program that helps users find recipes based on the ingredients they have on hand. This tool is designed for intermediate Python learners to practice file handling, JSON parsing, and conditional logic.

## Features

- **Ingredient-Based Recipe Search**: Enter a list of available ingredients, and the program will display recipes that can be made with those ingredients.
- **Detailed Recipe Information**: Shows recipe name, country of origin, description, preparation time, ingredients, and step-by-step instructions.
- **JSON Data Handling**: Reads recipes from a JSON file to dynamically load and search recipes.

## Requirements

- Python 3.x
- `recipes.json` file containing recipe data (formatted as per project requirements)

## Installation

1. Clone this repository or download the code files.
    ```bash
    git clone https://github.com/username/recipe-finder.git
    cd recipe-finder
    ```

2. Ensure that Python 3.x is installed:
    ```bash
    python --version
    ```

3. Ensure that the `recipes.json` file is in the same directory as the `recipe_finder.py` script.

## Usage

1. Run the `recipe_finder.py` script:
    ```bash
    python recipe_finder.py
    ```

2. Enter a list of ingredients, separated by commas (e.g., `rice, saffron, seafood,....`).
3. The program will display recipes that can be made using the specified ingredients, along with details like description, preparation time, instructions, and a video link if available.

## Example Workflow

1. Run the program.
2. Input ingredients you have at home, such as `rice, saffron, seafood, chicken, vegetables`.
3. If recipes match the ingredients you entered, the program will list them with all necessary details, including steps to follow for cooking.

## Files

- `recipe_finder.py`: The main Python script that implements the recipe search functionality.
- `recipes.json`: JSON file containing the recipe data with fields like `name`, `ingredients`, `country`, and `details`.

## License

This project is licensed under the MIT License.
