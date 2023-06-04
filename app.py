from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    pokemon_types = [
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
        "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
        "Dragon", "Dark", "Steel", "Fairy"
    ]

    type_effectiveness = {
        'Normal': ['green', 'green', 'green', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'green', 'green', 'green', 'grey', 'green', 'green', 'green', 'green'],
        'Fire': ['green', 'grey', 'blue', 'red', 'green', 'green', 'green', 'green', 'grey', 'grey', 'green', 'red', 'grey', 'green', 'green', 'green', 'grey', 'red'],
        'Water': ['green', 'red', 'grey', 'grey', 'red', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'green', 'green'],
        'Grass': ['green', 'red', 'blue', 'blue', 'grey', 'green', 'green', 'green', 'grey', 'grey', 'green', 'blue', 'red', 'green', 'green', 'green', 'green', 'green'],
        'Electric': ['green', 'green', 'red', 'grey', 'blue', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'green', 'green'],
        'Ice': ['green', 'red', 'blue', 'red', 'red', 'grey', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'],
        'Fighting': ['grey', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'green', 'red', 'red', 'green', 'green', 'green', 'green', 'red'],
        'Poison': ['green', 'green', 'green', 'red', 'green', 'green', 'green', 'grey', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'green', 'green'],
        'Ground': ['green', 'red', 'green', 'red', 'blue', 'green', 'green', 'blue', 'green', 'grey', 'green', 'red', 'grey', 'green', 'green', 'green', 'green', 'green'],
        'Flying': ['green', 'green', 'green', 'red', 'blue', 'green', 'blue', 'green', 'green', 'green', 'green', 'blue', 'grey', 'green', 'green', 'green', 'green', 'green'],
        'Psychic': ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'grey', 'green', 'green', 'green', 'grey', 'green', 'green', 'green'],
        'Bug': ['green', 'blue', 'green', 'blue', 'green', 'green', 'red', 'blue', 'grey', 'blue', 'green', 'green', 'red', 'green', 'green', 'green', 'blue', 'blue'],
        'Rock': ['green', 'blue', 'green', 'green', 'green', 'green', 'red', 'green', 'blue', 'red', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green'],
        'Ghost': ['grey', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'grey', 'green', 'green', 'green', 'green'],
        'Dragon': ['green', 'green', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'],
        'Dark': ['green', 'green', 'green', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'blue', 'green', 'green', 'grey', 'green', 'grey', 'green', 'green'],
        'Steel': ['green', 'blue', 'green', 'green', 'green', 'red', 'green', 'green', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'grey', 'green'],
        'Fairy': ['green', 'blue', 'green', 'red', 'green', 'green', 'green', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'green']
    }

    return render_template('index.html', pokemon_types=pokemon_types, type_effectiveness=type_effectiveness)

if __name__ == '__main__':
    app.run(debug=True)
