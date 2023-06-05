document.addEventListener('DOMContentLoaded', (event) => {
    let pokemonTypes = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy'];

    let colorIndex = {};
    let colors = ['white', 'green', 'red', 'blue', 'grey'];
	// let colors = ['grey', 'white', 'green', 'red', 'black'];

    pokemonTypes.forEach(type => {
        let btnUnhide = document.getElementById(`unhide-${type}`);
        btnUnhide.addEventListener('click', () => {
            pokemonTypes.forEach(otherType => {
                let button = document.getElementById(`${type}-${otherType}`);
                button.classList.remove('hidden');
            });
        });

		pokemonTypes.forEach(otherType => {
			let cell = document.getElementById(`cell-${type}-${otherType}`);
				cell.style.backgroundColor = 'white'; // 'lightgrey';
				colorIndex[`${type}-${otherType}`] = 0;
				cell.addEventListener('click', () => {
					colorIndex[`${type}-${otherType}`] = (colorIndex[`${type}-${otherType}`] + 1) % colors.length;
					cell.style.backgroundColor = colors[colorIndex[`${type}-${otherType}`]];
				});
			});
    });
});

function toggleText(event) {
  event.preventDefault();
  var moreText = document.getElementById("more");
  var linkText = document.getElementById("read-more-link");

  var expandableText = document.querySelector(".expandable-text");

  if (moreText.style.display === "none") {
    moreText.style.display = "inline";
    linkText.innerHTML = "Collapse";
    expandableText.style.maxHeight = "none";
  } else {
    moreText.style.display = "none";
    linkText.innerHTML = "Read more";
    expandableText.style.maxHeight = "60px";
  }
}