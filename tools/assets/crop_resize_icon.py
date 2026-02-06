
#!/usr/bin/env python3
Crop by alpha and resize to an exact target size.

This is useful after generating large icons (1024/1792) with transparent background.

Usage:
  python tools/assets/crop_resize_icon.py input.png output.png --w 512 --h 768 --pad 12

Notes:
- Crops to alpha bbox, expands by pad, then fits into target canvas with padding preserved.
- Keeps transparent background.

from __future__ import annotations

import argparse
from PIL import Image


def alpha_bbox(img: Image.Image, threshold: int = 8):
    a = img.convert("RGBA").split()[-1]
    bw = a.point(lambda p: 255 if p > threshold else 0, mode="L")
    return bw.getbbox()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--w", type=int, required=True)
    ap.add_argument("--h", type=int, required=True)
    ap.add_argument("--pad", type=int, default=12)
    args = ap.parse_args()

    img = Image.open(args.input).convert("RGBA")
    bbox = alpha_bbox(img)
    if bbox is None:
        raise SystemExit("Image seems fully transparent; nothing to crop.")

    l, t, r, b = bbox
    l = max(0, l - args.pad)
    t = max(0, t - args.pad)
    r = min(img.size[0], r + args.pad)
    b = min(img.size[1], b + args.pad)
    cropped = img.crop((l, t, r, b))

    # fit to target while keeping aspect ratio
    target = Image.new("RGBA", (args.w, args.h), (0, 0, 0, 0))
    cw, ch = cropped.size
    scale = min(args.w / cw, args.h / ch)
    nw, nh = max(1, int(cw * scale)), max(1, int(ch * scale))
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)

    x = (args.w - nw) // 2
    y = (args.h - nh) // 2
    target.alpha_composite(resized, (x, y))
    target.save(args.output)


if __name__ == "__main__":
    main()
