"""Init."""
from pathlib import Path
from .load_text import load_text

__version__ = "0.1.3"

# pylint: disable=invalid-name
cdir = Path(__file__).parent
hlm_zh = load_text(cdir / "340-脂砚斋重批红楼梦.txt")
hlm_en = load_text(cdir / "david-hawks-the-story-of-the-stone.txt")
hlm_en1 = load_text(cdir / "yang-hlm.txt")
hlm_en2 = load_text(cdir / "joly-hlm.txt")

fangfang_en = load_text(cdir / "fangfang-en.txt")
fangfang_zh = load_text(cdir / "fangfang-zh.txt")
