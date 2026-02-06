    ---
    name: art-ui-style
    description: Visual style guide prompts for generating UI and game art (Diablo 2 vibe)
    compatibility: opencode
    ---
    ## Style pillars
- Dark gothic fantasy (Diablo 2 vibe): stone, iron, worn leather, carved frames.
- High readability: strong silhouettes, limited saturated colors, clear rarity colors.
- Not modern-flat, not neon, not anime.

## Universal prompt add-on (use in every prompt)
- "dark gothic fantasy UI, Diablo 2 inspired, worn stone and iron frame, subtle parchment texture, high contrast readable, minimal glow, no modern flat design, no neon"

## Negative prompt (always)
- "modern flat UI, neon cyberpunk, anime, glossy 3D plastic, photoreal faces, watermark, signature, text, logos"

## UI components prompts
1) Inventory panel
   - "inventory panel UI, carved stone border, iron rivets, dark parchment background, subtle grime, medieval gothic, game interface, empty slots grid"
2) Tooltip frame
   - "item tooltip frame, ornate gothic border, parchment interior, subtle noise, high readability, no text"
3) Buttons
   - "gothic game button, stone + iron, bevelled edges, hover glow very subtle, icon-only"

## Item icons prompts
- "isometric item icon, hand-painted, Diablo 2 style, muted palette, strong silhouette, clean edges, transparent background"

## Export rules
- Prefer transparent PNG for icons/frames.
- Avoid text inside images (text is rendered in UI).



## Icon contract (must follow)

For any `icon/*` assets (items, runes, gems, potions, character icons):

- **PNG RGBA** with **fully transparent background** (alpha).
- **No UI panels / inventory grids / frames / cards / vignettes** in icon assets.
- Keep safe padding (8–12 px or ~10–14%) so UI does not clip silhouettes.
- Respect inventory footprint sizes from `docs/style/ASSET_SPECS.md`:
  - 1 cell = 128×128 (base) or 256×256 (hi-res)
  - Output dimensions must be exactly `W*cell × H*cell`.

Extra negative prompt for item icons:
- "no inventory grid, no slot frame, no UI panel, no border, no card, no vignette, no background"
