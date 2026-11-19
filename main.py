"""Emit the front page for the news-image-20261119 entry.

The picture itself lives in this repository as entry.png: a single page
summing up Thursday 19 November 2026. This script only moves those bytes
into the output folder the grader looks at. It talks to nothing on the
network and always produces the same file, run after run.
"""

import os
import sys
from pathlib import Path

PICTURE_NAME = "entry.png"
FALLBACK_FOLDER = "/output"


def locate_picture() -> Path:
    """Find the image sitting next to this script."""
    candidate = Path(__file__).resolve().parent / PICTURE_NAME
    if not candidate.is_file():
        raise SystemExit(f"cannot find {PICTURE_NAME} beside this script")
    return candidate


def destination_folder() -> Path:
    """Work out where the finished image belongs."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_FOLDER
    target = Path(chosen)
    try:
        target.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output folder {target}: {exc}")
    if not target.is_dir():
        raise SystemExit(f"output location {target} is not a folder")
    return target


def publish() -> int:
    """Read the stored picture and write it out unchanged."""
    picture = locate_picture()
    payload = picture.read_bytes()
    if len(payload) == 0:
        raise SystemExit(f"{PICTURE_NAME} is empty, refusing to emit it")
    out_path = destination_folder() / PICTURE_NAME
    out_path.write_bytes(payload)
    landed = out_path.stat().st_size
    if landed != len(payload):
        raise SystemExit(
            f"wrote {landed} bytes to {out_path}, expected {len(payload)}"
        )
    print(f"wrote {len(payload)} bytes to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(publish())
