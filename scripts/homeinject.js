const links = document.getElementsByClassName("homelink");

for(let link of links) {
    link.href = window.location.origin;
}

document.getElementsByClassName("logo")[0].onclick = () => {
    window.location.href = window.location.origin
}