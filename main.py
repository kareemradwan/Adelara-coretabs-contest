from flask import Flask, render_template, url_for, request
from meals import Meals, MealsStore

app = Flask(__name__)

dummy_meals = [
    Meals(
        1,
        'Pizza',
        1,
        [
            'Fromage',
            'Thon',
            'Olive',
        ],
        'https://images.pexels.com/photos/724216/pexels-photo-724216.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        200
    ),
    Meals(
        2,
        'Sandwich',
        1,
        [
            'Fromage',
            'Viande Hachée',
            'Frittes',
            'Omelette',
            'Salade'
        ],
        'https://images.pexels.com/photos/357746/pexels-photo-357746.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        140
    ),
    Meals(
        3,
        'Hamburger',
        1,
        [
            'Fromage',
            'Viande Hachée',
            'Frittes',
            'Omelette',
            'Salade'
        ],
        'https://images.pexels.com/photos/1639562/pexels-photo-1639562.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        120
    ),
]

meals = MealsStore(dummy_meals)
meals.get_all()


@app.route('/')
def index():
    return render_template('index.html', meals=dummy_meals)


@app.route('/details/<int:id>', methods=["GET", "POST"])
def details(id):
    if request.method == "GET":
        meal = meals.get_details(id)
        return render_template('details.html', meal=meal)

