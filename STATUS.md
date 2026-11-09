# Pokémon Tamagotchi V7 — Sprites offline

- 9 PNGs originais recuperados de `PokeAPI/sprites`, caminhos `sprites/pokemon/1.png` a `9.png`.
- 9/9 imagens PNG decodificadas e verificadas com Pillow; todas 96×96 e com transparência.
- SHA-256 individual em `assets/sprites/integrity.json`.
- HTML usa `assets/sprites/{id}.png` e não contém fallback remoto.
- Sintaxe JavaScript validada com `node --check`.
- Teste estático de disponibilidade offline: aprovado (recursos locais presentes e íntegros).
- Teste de interação em Chromium: **não executado**; navegador do ambiente bloqueia navegação local (`ERR_BLOCKED_BY_ADMINISTRATOR`).
- Teste real no iPhone: pendente.
