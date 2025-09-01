const games = [
  { id: 0, name: "Minecraft", file: "/games/minecraft.html", icon: "https://cdn2.steamgriddb.com/icon/bf6423635e56a99e9df17852c6bfadca/32/512x512.png", banner: "https://mmos.com/wp-content/uploads/2015/11/minecraft-banner.jpg", desc: "Minecraft Unblocked lets you dive into the ultimate sandbox adventure, free from restrictions. Whether you're crafting towering castles or surviving the night against mobs, this version of Minecraft is perfect for playing at school or work—no downloads, no logins, just pure creativity. Build, mine, and explore endless worlds right in your browser. If you're looking for a fun and free way to enjoy the game, Minecraft Unblocked is the best way to play online. Start building today—anytime, anywhere!"},
  { id: 1, "name":"Cookie Clicker","file":"/games/cookieclicker.html","icon":"https://play-lh.googleusercontent.com/Z1MOuuiD05ZN5LkVmMEvKF0mqAc-FknaQ2j8s4dZiO-LSPQX4EEA3RVJdlQEtxe96ok","banner":"https://cdn2.steamgriddb.com/hero_thumb/6b7d0fc39acc509d5910db3d0af96052.jpg","desc":"Cookie Clicker Unblocked is the addictive idle game where you bake as many cookies as possible by simply clicking. Start with one giant cookie, click to earn your first treats, then unlock upgrades, factories, and grandmas to keep the cookies flowing even while you’re not clicking.\n\n🎮 How to Play\n\nClick the cookie to generate your first batch.\n\nBuy upgrades to boost your production rate.\n\nAutomate with grandmas, farms, and factories.\n\nKeep growing until your cookie empire takes over the galaxy!\n\n⭐ Features\n\nSimple but endlessly addictive gameplay.\n\nUnlock achievements and rare upgrades.\n\nPlay instantly in your browser, no downloads needed.\n\n100% free and school-safe.\n\n🚀 Why Play Cookie Clicker Unblocked?\n\nCookie Clicker is perfect when you want a fun, stress-free game you can leave running in the background. Since this version is unblocked, you can play at school, work, or anywhere without restrictions. Grow your cookie empire and see how many cookies you can bake!\n\n👉 Play Cookie Clicker Unblocked now and start your sweet adventure."},
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

