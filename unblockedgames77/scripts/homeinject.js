const links = document.getElementsByClassName("homelink");

for(let link in links) {
    link.href = link.href = window.location.origin;
}