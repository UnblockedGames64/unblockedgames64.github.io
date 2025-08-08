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

// Append the window to the body
document.body.appendChild(incognitoWindow);

function openIncognitoWindow() {
    // Implement functionality to show/hide or animate the incognito window here
    incognitoWindow.style.opacity = incognitoWindow.style.opacity === '1' ? '0' : '1';
    incognitoWindow.style.right = incognitoWindow.style.right === '10px' ? '-300px' : '10px';
}