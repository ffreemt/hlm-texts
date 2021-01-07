"""Test sent_tokenizer."""
from pathlib import Path
from joblib import Memory
from hlm_texts import hlm_en
from hlm_texts import sent_tokenizer

memory = Memory(location=Path("~/joblib_cache").expanduser())
# cache location for sent_tokenizer: Path("~/joblib_cache").expanduser()
memory.clear(0)  # clear cache, no warning


def test_sent_tokenizer():
    """test_sent_tokenizer."""
    para_list = hlm_en.splitlines()[:12]
    assert len(sent_tokenizer(para_list, 'en')) == 19

    assert len(sent_tokenizer("\n".join(para_list), 'en')) == 19
