const incognitoButton = document.createElement('button');
incognitoButton.classList.add('incognito-button', 'glass');
incognitoButton.innerHTML = `<img src="../assets/icons/mask.svg" />`;

// Add event listener to open incognito window
incognitoButton.onclick = openIncognitoWindow;

// Append the button to the body
document.body.appendChild(incognitoButton);

// Create the incognito window div element
const incognitoWindow = document.createElement('div');
incognitoWindow.id = 'incognito-window';
incognitoWindow.classList.add('glass');

incognitoWindow.innerHTML += `
    <h1>Tab Masker</h1>
    <button onclick="disguise('https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Drive_icon_%282020%29.svg/1147px-Google_Drive_icon_%282020%29.svg.png', 'Home - Google Drive')">Google Drive</button>
    <button onclick="disguise('https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Google_Classroom_Logo.svg/1200px-Google_Classroom_Logo.svg.png', 'Google Classroom')">Google Classroom</button>
    <button onclick="disguise('https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Google_Docs_logo_%282014-2020%29.svg/1481px-Google_Docs_logo_%282014-2020%29.svg.png', 'Google Docs')">Google Docs</button>
    `

function disguise(icon, title) {
    document.head.querySelector('title').innerHTML = title;
    document.head.querySelector('link[rel="icon"]').href = icon;
}

// Append the window to the body
document.body.appendChild(incognitoWindow);

function openIncognitoWindow() {
    // Implement functionality to show/hide or animate the incognito window here
    incognitoWindow.style.opacity = incognitoWindow.style.opacity === '1' ? '0' : '1';
    incognitoWindow.style.right = incognitoWindow.style.right === '10px' ? '-300px' : '10px';
}