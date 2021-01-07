"""Tokenizer str|List[str] to sents."""
# pylint:

from typing import (
    List,
    Optional,
    Union,
)

from pathlib import Path
from joblib import Memory
from polyglot.text import Detector

from .seg_text import seg_text

memory = Memory(location=Path("~/joblib_cache").expanduser())


# fmt: off
@memory.cache
def sent_tokenizer(
        text: Union[str, List[str]],
        lang: Optional[str] = None,
) -> List[str]:
    """Tokenizer str|List[str] to sents."""
    # fmt: on
    if isinstance(text, str):
        text = [text]

    if lang is None:
        lang = Detector(" ".join(text)).language.code

    res = []
    for elm in text:
        res.extend(seg_text(elm, lang=lang))

    return res
