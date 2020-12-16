"""Encode sents in batch of size b_size."""
from typing import Any, Optional

from tqdm.auto import trange
import numpy as np

embed: Any = None

def encoder(data: list, b_size: int = 100) -> np.ndarray:
    """Encode sents in batch of size b_size.

    >>> assert encoder(['test']).shape == (1, 512)
    """

    b_size = 100
    len_ = len(data)
    # quo, rem = divmod(len_, b_size)
    quo, _ = divmod(len_, b_size)

    # abcnews 1082168, ~9 hours in duanzi
    # misinformation abstract, 5501, ~30 min
    encoded_data: Optional[np.ndarray] = None

    # quo part
    for i in trange(quo):
        _ = data[i * b_size: (i + 1) * b_size]
        _ = np.array([elm for elm in embed(_)]).astype("float32")
        if encoded_data is None:
            encoded_data = _
        else:
            encoded_data = np.concatenate((encoded_data, _), axis=0)

    # rem part
    _ = data[quo * b_size:]
    _ = np.array([elm for elm in embed(_)]).astype("float32")
    if encoded_data is None:
        encoded_data = _
    else:
        encoded_data = np.concatenate((encoded_data, _), axis=0)

    return encoded_data
