import json

def load_recipes(filename):
    with open(filename, 'r') as file:
        recipes = json.load(file)
    return recipes

def find_recipes(available_ingredients, recipes):
    matching_recipes = []
    
    for recipe in recipes:
        # Convert ingredients in the recipe to lowercase for comparison
        recipe_ingredients = {item.lower() for item in recipe['ingredients']}
        
        # Check if all ingredients in the recipe are in the available ingredients
        if recipe_ingredients.issubset(available_ingredients):
            matching_recipes.append(recipe)
    
    return matching_recipes

def main():
    # Load recipes from the JSON file
    filename = '/Users/ibensusan3/Desktop/Portfolio /Python coding/Recipe finder/recipes.json'
    recipes = load_recipes(filename)
    
    # Ask the user to input ingredients
    ingredients_input = input("Enter a list of ingredients, separated by commas: ")
    available_ingredients = {ingredient.strip().lower() for ingredient in ingredients_input.split(',')}
    
    # Find matching recipes
    matching_recipes = find_recipes(available_ingredients, recipes)
    
    # Display matching recipes
    if matching_recipes:
        print("\nHere are some recipes you can make:\n")
        for recipe in matching_recipes:
            print(f"Recipe: {recipe['name']}")
            print(f"Country: {recipe['country']}")
            print(f"Description: {recipe['details']['description']}")
            print(f"Preparation Time: {recipe['details']['prepTime']}")
            print("Ingredients:", ", ".join(recipe['ingredients']))
            print("Instructions:")
            for step in recipe['details']['steps']:
                print(f"  - {step}")
            print(f"Video: {recipe['details'].get('video', 'No video available')}\n")
    else:
        print("No recipes found with the ingredients provided.")

if __name__ == "__main__":
    main()
