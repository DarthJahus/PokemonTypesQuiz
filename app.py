from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    pokemon_types = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']

    # rename to _new and remove _old from the other to have white, red, black, green color scheme.
    type_effectiveness = {
        "Normal": ["green", "green", "green", "green", "green", "blue", "green", "grey", "blue", "green", "green", "green", "green", "green", "green", "green", "green", "green"],
        "Fighting": ["red", "green", "blue", "blue", "green", "red", "blue", "grey", "red", "green", "green", "green", "green", "blue", "red", "green", "red", "blue"],
        "Flying": ["green", "red", "green", "green", "green", "blue", "red", "green", "blue", "green", "green", "red", "blue", "green", "green", "green", "green", "green"],
        "Poison": ["green", "green", "green", "blue", "blue", "blue", "green", "blue", "grey", "green", "green", "red", "green", "green", "green", "green", "green", "red"],
        "Ground": ["green", "green", "grey", "red", "green", "red", "blue", "green", "red", "red", "green", "blue", "red", "green", "green", "green", "green", "green"],
        "Rock": ["green", "blue", "red", "green", "blue", "green", "red", "green", "blue", "red", "green", "green", "green", "green", "red", "green", "green", "green"],
        "Bug": ["green", "blue", "blue", "blue", "green", "green", "green", "blue", "blue", "blue", "green", "red", "green", "red", "green", "green", "red", "blue"],
        "Ghost": ["grey", "green", "green", "green", "green", "green", "green", "red", "green", "green", "green", "green", "green", "red", "green", "green", "blue", "green"],
        "Steel": ["green", "green", "green", "green", "green", "red", "green", "green", "blue", "blue", "blue", "green", "blue", "green", "red", "green", "green", "red"],
        "Fire": ["green", "green", "green", "green", "green", "blue", "red", "green", "red", "blue", "blue", "red", "green", "green", "red", "blue", "green", "green"],
        "Water": ["green", "green", "green", "green", "red", "red", "green", "green", "green", "red", "blue", "blue", "green", "green", "green", "blue", "green", "green"],
        "Grass": ["green", "green", "blue", "blue", "red", "red", "blue", "green", "blue", "blue", "red", "blue", "green", "green", "green", "blue", "green", "green"],
        "Electric": ["green", "green", "red", "green", "grey", "green", "green", "green", "green", "green", "red", "blue", "blue", "green", "green", "blue", "green", "green"],
        "Psychic": ["green", "red", "green", "red", "green", "green", "green", "green", "blue", "green", "green", "green", "green", "blue", "green", "green", "grey", "green"],
        "Ice": ["green", "green", "red", "green", "red", "green", "green", "green", "blue", "blue", "blue", "red", "green", "green", "blue", "red", "green", "green"],
        "Dragon": ["green", "green", "green", "green", "green", "green", "green", "green", "blue", "green", "green", "green", "green", "green", "green", "red", "green", "grey"],
        "Dark": ["green", "blue", "green", "green", "green", "green", "green", "red", "green", "green", "green", "green", "green", "red", "green", "green", "blue", "blue"],
        "Fairy": ["green", "red", "green", "blue", "green", "green", "green", "green", "blue", "blue", "green", "green", "green", "green", "green", "red", "red", "green"]
    }
    
    # add _old and remove _new from the other to have green, blue, grey, red color scheme.
    type_effectiveness_old = {
        "Normal": ["grey", "grey", "grey", "grey", "grey", "red", "grey", "black", "red", "grey", "grey", "grey", "grey", "grey", "grey", "grey", "grey", "grey"],
        "Fighting": ["green", "grey", "red", "red", "grey", "green", "red", "black", "green", "grey", "grey", "grey", "grey", "red", "green", "grey", "green", "red"],
        "Flying": ["grey", "green", "grey", "grey", "grey", "red", "green", "grey", "red", "grey", "grey", "green", "red", "grey", "grey", "grey", "grey", "grey"],
        "Poison": ["grey", "grey", "grey", "red", "red", "red", "grey", "red", "black", "grey", "grey", "green", "grey", "grey", "grey", "grey", "grey", "green"],
        "Ground": ["grey", "grey", "black", "green", "grey", "green", "red", "grey", "green", "green", "grey", "red", "green", "grey", "grey", "grey", "grey", "grey"],
        "Rock": ["grey", "red", "green", "grey", "red", "grey", "green", "grey", "red", "green", "grey", "grey", "grey", "grey", "green", "grey", "grey", "grey"],
        "Bug": ["grey", "red", "red", "red", "grey", "grey", "grey", "red", "red", "red", "grey", "green", "grey", "green", "grey", "grey", "green", "red"],
        "Ghost": ["black", "grey", "grey", "grey", "grey", "grey", "grey", "green", "grey", "grey", "grey", "grey", "grey", "green", "grey", "grey", "red", "grey"],
        "Steel": ["grey", "grey", "grey", "grey", "grey", "green", "grey", "grey", "red", "red", "red", "grey", "red", "grey", "green", "grey", "grey", "green"],
        "Fire": ["grey", "grey", "grey", "grey", "grey", "red", "green", "grey", "green", "red", "red", "green", "grey", "grey", "green", "red", "grey", "grey"],
        "Water": ["grey", "grey", "grey", "grey", "green", "green", "grey", "grey", "grey", "green", "red", "red", "grey", "grey", "grey", "red", "grey", "grey"],
        "Grass": ["grey", "grey", "red", "red", "green", "green", "red", "grey", "red", "red", "green", "red", "grey", "grey", "grey", "red", "grey", "grey"],
        "Electric": ["grey", "grey", "green", "grey", "black", "grey", "grey", "grey", "grey", "grey", "green", "red", "red", "grey", "grey", "red", "grey", "grey"],
        "Psychic": ["grey", "green", "grey", "green", "grey", "grey", "grey", "grey", "red", "grey", "grey", "grey", "grey", "red", "grey", "grey", "black", "grey"],
        "Ice": ["grey", "grey", "green", "grey", "green", "grey", "grey", "grey", "red", "red", "red", "green", "grey", "grey", "red", "green", "grey", "grey"],
        "Dragon": ["grey", "grey", "grey", "grey", "grey", "grey", "grey", "grey", "red", "grey", "grey", "grey", "grey", "grey", "grey", "green", "grey", "black"],
        "Dark": ["grey", "red", "grey", "grey", "grey", "grey", "grey", "green", "grey", "grey", "grey", "grey", "grey", "green", "grey", "grey", "red", "red"],
        "Fairy": ["grey", "green", "grey", "red", "grey", "grey", "grey", "grey", "red", "red", "grey", "grey", "grey", "grey", "grey", "green", "green", "grey"]
    }

    return render_template('index.html', pokemon_types=pokemon_types, type_effectiveness=type_effectiveness)

if __name__ == '__main__':
    app.run(debug=True)
