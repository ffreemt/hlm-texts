""" init """
from pathlib import Path
from .load_text import load_text

__version__ = "0.1.1"

cdir = Path(__file__).parent
hlm_zh = load_text(cdir / "340-脂砚斋重批红楼梦.txt")
hlm_en = load_text(cdir / "david-hawks-the-story-of-the-stone.txt")

fangfang_en = load_text(cdir / "fangfang-en.txt")
fangfang_zh = load_text(cdir / "fangfang-zh.txt")