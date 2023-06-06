document.addEventListener('DOMContentLoaded', (event) => {
    let pokemonTypes = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy'];

    let colorIndex = {};
    let colors = ['#F7F7F7', 'green', 'red', 'blue', 'grey'];
	// let colors = ['grey', 'white', 'green', 'red', 'black'];

    pokemonTypes.forEach(type => {
        let btnUnhide = document.getElementById(`unhide-${type}`);
        btnUnhide.addEventListener('click', () => {
            let score = 0;
            pokemonTypes.forEach(otherType => {
                let answer = document.getElementById(`${type}-${otherType}`);
                answer.classList.toggle('hidden');
                let cell = document.getElementById(`cell-${type}-${otherType}`);
                if (answer.style.backgroundColor === cell.style.backgroundColor) {score++;};
            });
            if (btnUnhide.textContent === "Unhide") {
                btnUnhide.textContent = `${score} / 18 (Hide)`;
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

    let cells = document.getElementsByClassName('cell');
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener('mouseover', highlightHeaders);
        cells[i].addEventListener('mouseout', removeHighlightHeaders);
    };

    let btnScore = document.getElementById(`btnScore`);
    btnScore.addEventListener('click', () => {
        if (btnScore.textContent === 'Show score') {
            let score = 0;
            pokemonTypes.forEach(type => {
                pokemonTypes.forEach(otherType => {
                    let answer = document.getElementById(`${type}-${otherType}`);
                    let cell = document.getElementById(`cell-${type}-${otherType}`);
                    if (answer.style.backgroundColor === cell.style.backgroundColor) {
                        score++;
                    };
                });
            });
            let scorePercentage = ((score / 384) * 100).toFixed(2);
            btnScore.textContent = `${score} / 384 (${scorePercentage}%)`;
        } else {
            btnScore.textContent = 'Show score';
        };
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
    expandableText.style.maxHeight = "55px";
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
