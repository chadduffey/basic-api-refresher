from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Chips',
        'description': 'Tasty tasty chippies'
    },
    {
        'id': 2,
        'name': 'Bacon and Egg Sambo',
        'description': 'Breakfast of champions'
    }
]


@app.route("/")
def hello():
    return "Hello"


@app.route("/recipes", methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route("/recipes", methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }

    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED


@app.route("/recipes/<int:recipe_id>", methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route("/recipes/<int:recipe_id>", methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()
    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(recipe)


if __name__ == "__main__":
    app.run()
