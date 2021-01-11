"""Init."""
from pathlib import Path
from .load_text import load_text
from .seg_text import seg_text
from .sent_tokenizer import sent_tokenizer

__version__ = "0.1.6"

# pylint: disable=invalid-name
cdir = Path(__file__).parent
hlm_zh = load_text(cdir / "340-脂砚斋重批红楼梦.txt")
hlm_en = load_text(cdir / "david-hawks-the-story-of-the-stone.txt")
hlm_en1 = load_text(cdir / "yang-hlm.txt")
hlm_en2 = load_text(cdir / "joly-hlm.txt")

fangfang_en = load_text(cdir / "fangfang-en.txt")
fangfang_zh = load_text(cdir / "fangfang-zh.txt")

# hlm_zh_sents = sent_tokenizer(hlm_zh, 'zh')
# hlm_en_sents = sent_tokenizer(hlm_en, 'en')
# hlm_en1_sents = sent_tokenizer(hlm_en1, 'en')
# hlm_en2_sents = sent_tokenizer(hlm_en2, 'en')

# fangfang_en_sents = sent_tokenizer(fangfang_en, 'en')
# fangfang_zh_sents = sent_tokenizer(fangfang_zh, 'zh')

__all__ = (
    "load_text",
    "seg_text",
    "sent_tokenizer",
)
