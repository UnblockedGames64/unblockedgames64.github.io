const games = [
  { id: 0, name: "Minecraft", file: "/games/minecraft.html", icon: "https://cdn2.steamgriddb.com/icon/bf6423635e56a99e9df17852c6bfadca/32/512x512.png", banner: "https://mmos.com/wp-content/uploads/2015/11/minecraft-banner.jpg", desc: "Minecraft Unblocked lets you dive into the ultimate sandbox adventure, free from restrictions. Whether you're crafting towering castles or surviving the night against mobs, this version of Minecraft is perfect for playing at school or work—no downloads, no logins, just pure creativity. Build, mine, and explore endless worlds right in your browser. If you're looking for a fun and free way to enjoy the game, Minecraft Unblocked is the best way to play online. Start building today—anytime, anywhere!"}
];

for(let gamei in games) {
    let game = games[gamei];
    document.getElementById("games-sidebar").innerHTML += `<a href='${window.location.origin}${game.file}'><img src='${game.icon}'>${game.name}</a>`
}

if(document.getElementById("new")) {
  for(let i = games.length-1; i > games.length - 10; i--) {
    if(games[i]) {
      document.getElementById("new").innerHTML += `<div onclick="window.location.href = '${window.location.origin}${games[i].file}'" class="game-card"><img src="${games[i].banner}"><h1>${games[i].name}</h1><div class="desc">${games[i].desc}</div></div>`;
    }
  }
}

if(document.getElementById("all")) {
  for(let i = 0; i < games.length; i++) {
    if(games[i]) {
      document.getElementById("all").innerHTML += `<div onclick="window.location.href = '${window.location.origin}${games[i].file}'" class="game-icon"><img src="${games[i].icon}"><h1 class="glass">${games[i].name}</h1></div>`;
    }
  }
}

