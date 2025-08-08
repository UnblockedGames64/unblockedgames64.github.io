const games = [
  { name: "Minecraft", file: "/games/minecraft.html", icon: "https://cdn2.steamgriddb.com/icon/bf6423635e56a99e9df17852c6bfadca/32/512x512.png" }
];

for(let gamei in games) {
    let game = games[gamei];
    document.getElementById("games-sidebar").innerHTML += `<a href='${window.location.origin}${game.file}'><img src='${game.icon}'>${game.name}</a>`
}
