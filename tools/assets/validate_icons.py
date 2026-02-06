
#!/usr/bin/env python3
Validate `icon/*` PNGs for this repo.

Checks:
- PNG has alpha channel
- corners are transparent (common “background mistake”)
- dimensions match cell grid (128/256 per cell) unless explicitly excluded
- object bounding box keeps minimal padding from edges

Usage:
  python tools/assets/validate_icons.py path/to/icons [--cell 256] [--min-pad 8]

Exit code:
  0 = ok, 1 = warnings/errors found

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from typing import Iterable, List, Tuple

from PIL import Image


@dataclass
class Issue:
    path: str
    level: str  # "ERROR" or "WARN"
    message: str


def iter_png_files(root: str) -> Iterable[str]:
    if os.path.isfile(root) and root.lower().endswith(".png"):
        yield root
        return
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".png"):
                yield os.path.join(dirpath, name)


def has_alpha(img: Image.Image) -> bool:
    return img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info)


def alpha_channel(img: Image.Image) -> Image.Image:
    if img.mode == "RGBA":
        return img.split()[-1]
    if img.mode == "LA":
        return img.split()[-1]
    if img.mode == "P":
        # Convert paletted with transparency to RGBA
        return img.convert("RGBA").split()[-1]
    return img.convert("RGBA").split()[-1]


def bbox_from_alpha(a: Image.Image, threshold: int = 8) -> Tuple[int, int, int, int] | None:
    # threshold: alpha > threshold is considered "content"
    bw = a.point(lambda p: 255 if p > threshold else 0, mode="L")
    return bw.getbbox()


def validate_one(path: str, cell: int, min_pad: int) -> List[Issue]:
    issues: List[Issue] = []
    try:
        img = Image.open(path)
        img.load()
    except Exception as e:
        return [Issue(path, "ERROR", f"Cannot open image: {e}")]

    if not has_alpha(img):
        issues.append(Issue(path, "ERROR", "Image has no alpha channel (must be PNG RGBA with transparent background)."))
        # continue, but bbox checks won't make sense

    w, h = img.size

    # Corner transparency check (quick smoke test against “solid background”)
    a = alpha_channel(img)
    corners = [
        a.getpixel((0, 0)),
        a.getpixel((w - 1, 0)),
        a.getpixel((0, h - 1)),
        a.getpixel((w - 1, h - 1)),
    ]
    if any(c > 0 for c in corners):
        issues.append(Issue(path, "ERROR", "Corners are not fully transparent → likely a non-transparent background."))

    # Dimension multiple-of-cell check
    if (w % cell != 0) or (h % cell != 0):
        issues.append(
            Issue(
                path,
                "WARN",
                f"Dimensions {w}x{h} are not multiples of cell={cell}. "
                f"Expected W*{cell} × H*{cell} (see docs/style/ASSET_SPECS.md).",
            )
        )

    # Padding check vs content bbox
    bbox = bbox_from_alpha(a, threshold=8)
    if bbox is None:
        issues.append(Issue(path, "WARN", "Alpha bbox is empty (fully transparent?)"))
        return issues

    left, top, right, bottom = bbox
    pad_left = left
    pad_top = top
    pad_right = w - right
    pad_bottom = h - bottom
    if min(pad_left, pad_top, pad_right, pad_bottom) < min_pad:
        issues.append(
            Issue(
                path,
                "WARN",
                f"Content too close to edge (padding L{pad_left}/T{pad_top}/R{pad_right}/B{pad_bottom} < {min_pad}px). "
                "Increase safe padding so UI doesn't clip the silhouette.",
            )
        )

    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="File or directory with PNG icons")
    ap.add_argument("--cell", type=int, default=256, help="Cell size in pixels for hi-res export (default: 256)")
    ap.add_argument("--min-pad", type=int, default=8, help="Minimal safe padding in pixels (default: 8)")
    args = ap.parse_args()

    all_issues: List[Issue] = []
    for p in iter_png_files(args.path):
        all_issues.extend(validate_one(p, cell=args.cell, min_pad=args.min_pad))

    errors = [i for i in all_issues if i.level == "ERROR"]
    warns = [i for i in all_issues if i.level == "WARN"]

    for i in errors + warns:
        print(f"{i.level}: {i.path} — {i.message}")

    if errors:
        print(f"\nFAIL: {len(errors)} errors, {len(warns)} warnings.")
        return 1

    if warns:
        print(f"\nOK with warnings: {len(warns)} warnings.")
        return 1

    print("OK: all icons look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
