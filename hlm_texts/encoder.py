"""Encode sents in batch of size b_size."""
from typing import Callable, Iterable, Optional

# from tqdm.auto import tqdm  # trange
# .auto does not seem to work well with upyterlab
from tqdm import tqdm

import numpy as np
import more_itertools as mit
from logzero import logger

# embed: Any = None


# fmt: off
def encoder(
        # data: list,
        data: Iterable[str],
        embed: Optional[Callable] = None,
        b_size: int = 100,
) -> np.ndarray:
    # fmt: on
    """Encode sents in batch of size b_size.

    b_size for memory management when using google-use embed,
    the other embed has its own batch
    management, b_size wont affect memory management too much

    >>> assert encoder(['test']).shape == (1, 512)
    """
    if embed is None:
        logger.error(" embed is None, return empty np.ndarray.")
        logger.error("You need to plug in some embed method")
        return np.ndarray([0])

    # abcnews 1082168, ~9 hours in duanzi
    # misinformation abstract, 5501, ~30 min
    encoded_data: Optional[np.ndarray] = None

    for _ in tqdm(mit.chunked(data, b_size)):
        _ = list(_)
        _ = np.array(embed(_)).astype("float32")
        if encoded_data is None:
            encoded_data = _
        else:
            encoded_data = np.concatenate((encoded_data, _), axis=0)

    _ = """
    # b_size = 100
    len_ = len(data)
    quo, rem = divmod(len_, b_size)
    # quo, _ = divmod(len_, b_size)

    # quo part
    for i in trange(quo):
        _ = data[i * b_size: (i + 1) * b_size]
        _ = np.array(elm for elm in embed(_)).astype("float32")
        if encoded_data is None:
            encoded_data = _
        else:
            encoded_data = np.concatenate((encoded_data, _), axis=0)

    # rem part
    if rem:
        _ = data[quo * b_size:]
        _ = np.array(elm for elm in embed(_)).astype("float32")
        if encoded_data is None:
            encoded_data = _
        else:
            encoded_data = np.concatenate((encoded_data, _), axis=0)
    # """

    return encoded_data
