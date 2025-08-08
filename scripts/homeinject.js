const links = document.getElementsByClassName("homelink");

for(let link of links) {
    link.href = window.location.origin;
}