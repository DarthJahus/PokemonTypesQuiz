document.addEventListener('DOMContentLoaded', (event) => {
    let pokemonTypes = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy'];

    let colorIndex = {};
    let colors = ['white', 'green', 'red', 'blue', 'grey'];
	// let colors = ['grey', 'white', 'green', 'red', 'black'];

    pokemonTypes.forEach(type => {
        let btnUnhide = document.getElementById(`unhide-${type}`);
        btnUnhide.addEventListener('click', () => {
            pokemonTypes.forEach(otherType => {
                let answer = document.getElementById(`${type}-${otherType}`);
                answer.classList.toggle('hidden');
            });
            if (btnUnhide.textContent === "Unhide") {
                btnUnhide.textContent = "Hide";
            } else {
                btnUnhide.textContent = "Unhide";
            }
        });

		pokemonTypes.forEach(otherType => {
			let cell = document.getElementById(`cell-${type}-${otherType}`);
				cell.style.backgroundColor = '#F7F7F7'; // 'lightgrey';
				colorIndex[`${type}-${otherType}`] = 0;
				cell.addEventListener('click', () => {
					colorIndex[`${type}-${otherType}`] = (colorIndex[`${type}-${otherType}`] + 1) % colors.length;
					cell.style.backgroundColor = colors[colorIndex[`${type}-${otherType}`]];
				});
			});
    });

    let cells = document.getElementsByClassName("cell");
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("mouseover", highlightHeaders);
        cells[i].addEventListener("mouseout", removeHighlightHeaders);
    }
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

function highlightHeaders() {
    let parentRow = this.parentNode;
    let cellIndex = Array.prototype.indexOf.call(parentRow.children, this);
    let headers = document.getElementsByTagName("th");
    headers[cellIndex].classList.add("highlight-atk");
    parentRow.cells[0].classList.add("highlight-def");
}
function removeHighlightHeaders() {
    let headers = document.getElementsByTagName("th");
    for (let i = 0; i < headers.length; i++) {
        headers[i].classList.remove("highlight-atk");
        headers[i].classList.remove("highlight-def");
    }
}
