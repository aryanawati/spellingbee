import sys
import ctypes
import shutil
from pathlib import Path


FONT_DIR = Path(__file__).parent.parent / "assets" / "fonts"

FONT_PATHS = [
    "franklin-normal-600.ttf",
    "karnak-small-normal-400.ttf"
]


def load_fonts():
    for font_name in FONT_PATHS:
        font_path = FONT_DIR / font_name

        if sys.platform == "win32":
            ctypes.windll.gdi32.AddFontResourceExW(
                str(font_path),
                0x10,
                0
            )

        elif sys.platform == "darwin":
            font_dir = Path.home() / "Library" / "Fonts"
            destination = font_dir / font_name

            if not destination.exists():
                shutil.copy(font_path, destination)