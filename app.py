from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load recipes from JSON file
def load_recipes():
    with open('recipes.json') as f:
        return json.load(f)

recipes = load_recipes()

# Function to find recipes based on a single ingredient
def find_recipes_by_ingredient(ingredient):
    matched_recipes = []

    for recipe in recipes:
        if ingredient.lower() in [i.lower() for i in recipe['ingredients']]:
            matched_recipes.append(recipe)

    return matched_recipes

@app.route('/search', methods=['POST'])
def search_recipe():
    data = request.json
    ingredient = data.get('ingredient', '').strip()
    
    if not ingredient:
        return jsonify({"message": "No ingredient provided."}), 400

    matched_recipes = find_recipes_by_ingredient(ingredient)

    if matched_recipes:
        return jsonify(matched_recipes)
    else:
        return jsonify({"message": "No recipes found with the given ingredient."}), 404

if __name__ == '__main__':
    app.run(debug=True)