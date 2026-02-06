
# AI Asset Generation — item icons (how to not get it wrong)

This repo distinguishes **item icons** (`icon/*`) from **UI frames/panels** (`ui/*`).

If you want a Diablo-2-like inventory:
- items are just **transparent PNG icons** sized by `W×H` cells
- the inventory grid/slots are **separate UI assets**

## Non-negotiable rules for `icon/*`

- **PNG RGBA** with **fully transparent background**.
- **No** inventory grid, slot frame, UI panel, “card”, vignette, background gradient.
- No text baked into images.
- Keep safe padding (8–12 px or ~10–14%) so silhouettes aren't clipped.

Reference: `docs/style/ASSET_SPECS.md` → “Прозрачность и alpha” + “Размер предметов в сетке”.

## Recommended pipeline (works well with generators)

Because generators may not respect exact pixel sizes, do this:

1) **Generate big** (1024×1024 or 1024×1792 / 1792×1024) with transparent background.
2) **Post-process**:
   - crop by alpha bbox (keep padding)
   - resize to exact `W*cell × H*cell` (cell = 256 for hi-res)
3) **Validate**:
   - `python tools/assets/validate_icons.py <icons-dir>`

## File naming (suggested)

```
client/src/assets/icons/items/sets/<set_slug>/<item_slug>__<W>x<H>__256.png
```

Examples:
- `.../wanderer_hood__2x2__256.png`
- `.../militia_blade__1x4__256.png`
- `.../wanderer_vest__2x3__256.png`

(We can add an atlas later; keep source icons first.)
