"""Test gen_tokens."""
# import os
# os.environ["JLNOCACHE"] = "1"  # to turn off joblib.Memory
# in setup?

import more_itertools as mit
from hlm_texts import fangfang_en, fangfang_zh, gen_tokens, list_tokens


def test_gen_tokens():
    """Test gen_tokens."""
    sent_numb = mit.ilen(gen_tokens(fangfang_en))
    para_numb = mit.ilen(gen_tokens(fangfang_en, gen_para=1, gen_sent=0))
    para_sent_numb = mit.ilen(gen_tokens(fangfang_en, gen_para=1))

    assert sent_numb == 5814
    assert para_numb == 885
    assert para_sent_numb == 5814 + 885

    assert len(list_tokens(fangfang_en)) == 5814
    assert len(list_tokens(fangfang_en, gen_para=1, gen_sent=0)) == 885


def test_gen_tokens_zh():
    """Test gen_tokens."""
    sent_numb = mit.ilen(gen_tokens(fangfang_zh))
    para_numb = mit.ilen(gen_tokens(fangfang_zh, gen_para=1, gen_sent=0))
    para_sent_numb = mit.ilen(gen_tokens(fangfang_zh, gen_para=1))

    assert sent_numb == 4818
    assert para_numb == 745
    assert para_sent_numb == 4818 + 745

    assert len(list_tokens(fangfang_zh)) == 4818
    assert len(list_tokens(fangfang_zh, gen_para=1, gen_sent=0)) == 745
