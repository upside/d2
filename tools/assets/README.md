
# Asset tools (icons)

These scripts help keep generated icons consistent with `docs/style/ASSET_SPECS.md`.

## Validate icons

Checks alpha transparency, common background mistakes, cell-multiple dimensions, and safe padding.

```bash
python tools/assets/validate_icons.py path/to/icons --cell 256 --min-pad 8
```

## Crop + resize a generated icon

If your generator outputs 1024/1792 canvases, use this to crop by alpha and fit into the exact W×H export.

```bash
python tools/assets/crop_resize_icon.py input.png output.png --w 512 --h 768 --pad 12
```
