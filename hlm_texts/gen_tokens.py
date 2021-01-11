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

from polyglot.text import Detector
from polyglot.detect.base import logger as polyglot_logger
from logzero import logger

# from phrase_tokenizer import phrase_tok
from hlm_texts.sent_tokenizer import _sent_tokenizer

polyglot_logger.setLevel("ERROR")


# fmt: off
def gen_token(
        text: Union[str, List[str]],
        label: str = "",
        lang: Optional[str] = None,
        gen_para: bool = False,
        gen_sent: bool = True,
        gen_phrase: bool = False,
        # ) -> Generator[Tuple[str, str, int, str], None, None]:
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
                ...
                # for phrase in phrase_tok(sent):
                # yield phrase, label, idx + 1, 'phra'
