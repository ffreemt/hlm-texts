"""Genereate tokens from text/list of text.

dz ~/myapps/fastapi-s hlm-faiss.ipynb
"""
# pylint: disable=too-many-arguments

from typing import (
    # Generator,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

import os
from pathlib import Path
from joblib import Memory
from polyglot.text import Detector
from polyglot.detect.base import logger as polyglot_logger
from logzero import logger

# from phrase_tokenizer import phrase_tok
from hlm_texts.sent_tokenizer import _sent_tokenizer

polyglot_logger.setLevel("ERROR")
if os.environ.get("JLNOCACHE") is None:
    _ = Path("~/joblib_cache").expanduser()
else:
    _ = None  # no cache if JLNOCACHE is set for testing
memory = Memory(location=_, verbose=0)


# fmt: off
def gen_tokens(
        text: Union[str, List[str]],
        label: str = "",
        lang: Optional[str] = None,
        gen_para: Union[int, bool] = False,
        gen_sent: Union[int, bool] = True,
        gen_phrase: Union[int, bool] = False,
) -> Iterator[Tuple[str, str, int, str]]:
    # fmt: on
    """Genereate tokens from text/list of text."""
    if isinstance(text, str):
        text = [elm.strip() for elm in text.splitlines() if elm.strip()]

    if lang is None:
        lang = Detector(" ".join(text)).language.code
        logger.debug("Deteced lang: %s", lang)

    if gen_para:
        for idx, para in enumerate(text):
            yield para, label, idx + 1, 'para'
    if gen_sent:
        for idx, para in enumerate(text):
            for sent in _sent_tokenizer(para, lang):
                yield sent, label, idx + 1, 'sent'
    if gen_phrase:
        for idx, para in enumerate(text):
            for sent in _sent_tokenizer(para, lang):
                raise Exception(
                    "need to install phrase_tokenizer"
                    "which is dependant of benepar"
                )
                # for phrase in phrase_tok(sent):
                # yield phrase, label, idx + 1, 'phra'

@memory.cache
# fmt: off
def list_tokens(
        text: Union[str, List[str]],
        label: str = "",
        lang: Optional[str] = None,
        gen_para: Union[int, bool] = False,
        gen_sent: Union[int, bool] = True,
        gen_phrase: Union[int, bool] = False,
) -> List[Tuple[str, str, int, str]]:
    # fmt: on
    """List tokens with memoization."""
    return [*gen_tokens(
        text,
        label,
        lang,
        gen_para,
        gen_sent,
        gen_phrase,
    )]
