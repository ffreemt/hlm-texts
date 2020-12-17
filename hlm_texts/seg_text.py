"""Split text to sentences.

Use sentence_splitter if supported,
else use polyglot.text.Text
"""
from typing import List, Optional

from tqdm.auto import tqdm
from polyglot.text import Detector, Text
from sentence_splitter import split_text_into_sentences

# fmt: off
# use sentence_splitter if supported
LANG_S = ["ca", "cs", "da", "nl", "en", "fi", "fr", "de",
          "el", "hu", "is", "it", "lv", "lt", "no", "pl",
          "pt", "ro", "ru", "sk", "sl", "es", "sv", "tr"]
# fmt: on


def seg_text(text: str, lang: Optional[str] = None, qmode: bool = False, maxlines: int = 1000) -> List[str]:
    """
    Split text to sentences.

    Use sentence_splitter if supported,
    else use polyglot.text.Text.sentences

    qmode: skip split_text_into_sentences if True, default False
        vectors for all books are based on qmode=False.
        qmode=True is for quick test purpose only

    maxlines (default 1000), threhold for turn on tqdm progressbar
        set to <1 or a large number to turn it off
    """
    if lang is None:
        lang = Detector(text).language.code

    if not qmode and lang in LANG_S:
        _ = []
        lines = text.splitlines()
        if maxlines > 1 and len(lines) > maxlines:
            for para in tqdm(lines):
                if para.strip():
                    _.extend(split_text_into_sentences(para, lang))
        else:
            for para in lines:
                if para.strip():
                    _.extend(split_text_into_sentences(para, lang))
        return _

        # return split_text_into_sentences(text, lang)

    return [elm.string for elm in Text(text, lang).sentences]
