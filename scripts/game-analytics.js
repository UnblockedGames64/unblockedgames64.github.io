const WEBAPP_URL = "https://script.google.com/macros/s/AKfycby03yhMtBqH7RTvnjljfRz8g_n-6WLehz-qn_snZXjIaZXsm8p58BF3FQt4rHDU4qhh/exec"; // Replace with your Apps Script Web App URL
let rowData;

if(!localStorage.liked) {
    localStorage.liked = JSON.stringify([false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, ]);
}

// Function to increment a specific cell
async function incrementCell(sheetName, cell) {
  try {
    const formData = new FormData();
    formData.append("action", "increment");
    formData.append("cell", cell);
    formData.append("sheet", sheetName);

    const response = await fetch(WEBAPP_URL, {
      method: "POST",
      body: formData
    });

    const result = await response.json();
    return result;
  } catch (error) {
    console.error("Error incrementing cell:", error);
  }
}

// Function to fetch an entire row as an array
async function fetchRow(sheetName, rowNumber) {
  try {
    const response = await fetch(`${WEBAPP_URL}?action=fetchRow&sheet=${sheetName}&row=${rowNumber}`);
    const result = await response.json();
    return result.row; // returns array of cell values
  } catch (error) {
    console.error("Error fetching row:", error);
  }
}

async function fetchSheet(sheetName) {
  try {
    const response = await fetch(`${WEBAPP_URL}?action=fetchSheet&sheet=${sheetName}`);
    const result = await response.json();
    return result.matrix; // returns 2D array
  } catch (error) {
    console.error("Error fetching sheet:", error);
  }
}

function getIdByName(name) {
  const item = games.find(obj => obj.name.toLowerCase() === name.toLowerCase());
  return item ? item.id : null; // returns null if not found
}

async function likeGame() {
    let liked = JSON.parse(localStorage.liked);
    if(JSON.parse(localStorage.liked)[getIdByName(document.getElementsByClassName("gamebar")[0].firstChild.innerHTML)] === false) {
        liked[getIdByName(document.getElementsByClassName("gamebar")[0].firstChild.innerHTML)] = true;

        await incrementCell("Sheet1", "B" + String(getIdByName(document.getElementsByClassName("gamebar")[0].firstChild.innerHTML) + 1));
        document.getElementById("stats").innerHTML = `${rowData[0] + 1} Views<br>${rowData[1] + 1} Likes`

        localStorage.liked = JSON.stringify(liked);
    } 
}

if(document.getElementById("suggested")) {
    for(let i = 0; i < 5; i++) {
        random = Math.round(Math.random() * (games.length - 1) );

        document.getElementById("suggested").innerHTML += `<div onclick="window.location.href = '${window.location.origin}${games[random].file}'" class="game-icon"><img src="${games[random].icon}"><h1 class="glass">${games[random].name}</h1></div>`
    }
}
