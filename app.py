from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

# Load recipes from JSON file
def load_recipes():
    with open('recipes.json') as f:
        return json.load(f)

recipes = load_recipes()

# Function to find recipes based on available ingredients
def find_recipes(available_ingredients):
    available_set = set(available_ingredients)
    matched_recipes = []

    for recipe in recipes:
        recipe_set = set(recipe['ingredients'])
        if recipe_set.issubset(available_set):
            matched_recipes.append(recipe)

    return matched_recipes

@app.route('/generate', methods=['POST'])
def generate_recipe():
    data = request.json
    available_ingredients = data.get('ingredients', [])
    
    matched_recipes = find_recipes(available_ingredients)

    if matched_recipes:
        selected_recipe = random.choice(matched_recipes)
        return jsonify(selected_recipe)
    else:
        return jsonify({"message": "No recipes found with the given ingredients."}), 404

if __name__ == '__main__':
    app.run(debug=True)