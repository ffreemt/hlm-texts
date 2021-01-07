# hlm-texts [![Codacy Badge](https://api.codacy.com/project/badge/Grade/31c6bcb6723942a3bb12474cd7e74dac)](https://app.codacy.com/gh/ffreemt/hlm-texts?utm_source=github.com&utm_medium=referral&utm_content=ffreemt/hlm-texts&utm_campaign=Badge_Grade)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/hlm-texts.svg)](https://badge.fury.io/py/hlm-texts)

Hlm at your fingertips

This repo currently just has
  * `340-脂砚斋重批红楼梦.txt`: hlm_zh
  * `david-hawks-the-story-of-the-stone.txt`: hlm_en
  * `yang-hlm.txt`: hlm_en1
  * `joly-hlm.txt`: hlm_en2

It may expand to other versions. If you wish to have one particular version included, make a `pull request` (fork, upload files and click the pull request button) or provide a text file to me.

## Special Dependencies

`hlm_texts` depends on polyglot that in turn depends on `libicu`

To install `libicu`
### For Linux/OSX

E.g.
* Ubuntu: `sudo apt install libicu-dev`
* Centos: `yum install libicu`
* OSX: `brew install icu4c`

Then use `poetry` or `pip` to install ` PyICU pycld2 Morfessor`, e.g.
```bash
pip install PyICU pycld2 Morfessor
```
or
```python
poetry add PyICU pycld2 Morfessor
```
### For Windows

Download and install the `pyicu` and `pycld2` (possibly also `Morfessor`) whl packages for your OS/Python version from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyicu and https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycld2 (possibly also Morfessor https://www.lfd.uci.edu/~gohlke/pythonlibs/)

## Installation

`pip install hlm-texts`
or git clone the repo and install from the source
```bash
git clone
cd hlm-texts
pip install -r requirements.text
```

## Usage

```python
from hlm_texts import hlm_en, hlm_zh, hlm_en1, hlm_en2
```

`hlm_zh` and `hlm_en` are copies of `340-脂砚斋重批红楼梦.txt` and `david-hawks-the-story-of-the-stone.txt`, respectively, with blank lines removed and paragraphs retaind.

`sent_tokenizer`: to tokenize text or list of texts
```python
from hlm_texts import sent_tokenizer, hlm_en

hlm_en_sents = sent_tokenizer(hlm_en, lang="en")
```
Tokenizing long English texts for the first time can take a while (3-5 minutes for hlm_en, hlm_en1, hlm_en2). Subsequent operations are, however, instant since ``sent_tokenizer`` is cached in ``~/joblib_cache`` (\Users\xyz\joblib_cache` for `Windows 10`).

## Notes

The repo is for study purpose only. If you believe that your interests have been violated in any way, please let me know. I'll promptly follow it up with appropriate actions.