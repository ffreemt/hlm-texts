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


def seg_text(text: str, lang: Optional[str] = None, qmode: bool = False) -> List[str]:
    """
    Split text to sentences.

    Use sentence_splitter if supported,
    else use polyglot.text.Text.

    qmode: skip split_text_into_sentences if True, default False
    """

    if lang is None:
        lang = Detector(text).language.code

    if not qmode and lang in LANG_S:
        _ = []
        for para in tqdm(text.splitlines()):
            if para.strip():
                _.extend(split_text_into_sentences(para, lang))
        return _

        # return split_text_into_sentences(text, lang)

    return [elm.string for elm in Text(text, lang).sentences]
