"""
load text with best effort to determine encoding
"""

from typing import Union
from pathlib import Path

import cchardet
from logzero import logger


def load_text(filename: Union[str, Path]) -> str:
    """
    load text for given filepath
    """
    if not Path(filename).is_file():
        raise SystemExit(
            f"{Path(filename).resolve().as_posix()} does not exist or is not a file"
        )
    try:
        _ = cchardet.detect(Path(filename).read_bytes())
    except Exception as exc:
        logger.error("cchardet exc: %s, setting encoding to utf8", exc)
        _ = {"encoding": "utf8"}
    encoding = _["encoding"]

    try:
        cont = Path(filename).read_text(encoding)
    except Exception as exc:
        logger.error(" read_text exc: %s", exc)
        raise

    _ = [elm.strip() for elm in cont.splitlines() if elm.strip()]
    return "\n".join(_)
