const games = [
  { name: "Minecraft", file: "./games/minecraft.html" }
];

for(let gamei in games) {
    let game = games[gamei];
    document.getElementById("games-sidebar").innerHTML += `<a href='${game.file}'>${game.name}</a>`
}
