document.addEventListener('DOMContentLoaded', (event) => {
    let pokemonTypes = [
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
        "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
        "Dragon", "Dark", "Steel", "Fairy"
    ];

    let colorIndex = {};
    let colors = ['white', 'green', 'red', 'blue', 'grey'];

    pokemonTypes.forEach(type => {
        let btnUnhide = document.getElementById(`unhide-${type}`);
        btnUnhide.addEventListener('click', () => {
            pokemonTypes.forEach(otherType => {
                let button = document.getElementById(`${type}-${otherType}`);
                button.classList.remove('hidden');
            });
        });

        pokemonTypes.forEach(otherType => {
            let button = document.getElementById(`${type}-${otherType}`);
            button.style.backgroundColor = 'white';
            colorIndex[`${type}-${otherType}`] = 0;
            button.addEventListener('click', () => {
                colorIndex[`${type}-${otherType}`] = (colorIndex[`${type}-${otherType}`] + 1) % colors.length;
                button.style.backgroundColor = colors[colorIndex[`${type}-${otherType}`]];
            });
        });
    });
});
