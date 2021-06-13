"""Tokenize str|List[str] to sents."""
# pylint: disable=unused-argument

from typing import (
    List,
    Optional,
    Union,
)

from pathlib import Path
from joblib import Memory
from polyglot.text import Detector
from logzero import logger

from hlm_texts.seg_text import seg_text

memory = Memory(location=Path("~/joblib_cache").expanduser(), verbose=0)


# fmt: off
# @memory.cache(ignore=['debug'])
def _sent_tokenizer(
        text: Union[str, List[str]],
        lang: Optional[str] = None,
        debug: bool = False,  # when True, disable joblib.Memory.cache
) -> List[str]:
    # fmt: on
    """Tokenize str|List[str] to sents."""
    if isinstance(text, str):
        text = [text]

    if lang is None:
        try:
            lang = Detector(" ".join(text)).language.code
        except Exception as exc:
            logger.warning("polyglot.text.Detector exc: %s, setting to 'en'", exc)
            logger.info(" Try to pass lang (e.g. lang='en') to sent_tokenizer")
            lang = 'en'

    res = []
    for elm in text:
        res.extend(seg_text(elm, lang=lang))

    return res


sent_tokenizer = memory.cache(_sent_tokenizer, ignore=['debug'])
