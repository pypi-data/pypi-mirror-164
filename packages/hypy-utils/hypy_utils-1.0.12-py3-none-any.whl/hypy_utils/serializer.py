from __future__ import annotations

import io
import pickle
from pathlib import Path


def pickle_encode(obj: any, protocol=None, fix_imports=True) -> bytes:
    """
    Encode object to pickle bytes

    >>> by = pickle_encode({'function': pickle_encode})
    >>> len(by)
    57
    >>> decoded = pickle_decode(by)
    >>> by = decoded['function']({'meow': 565656})
    >>> pickle_decode(by)
    {'meow': 565656}
    """
    with io.BytesIO() as bio:
        pickle.dump(obj, bio, protocol=protocol, fix_imports=fix_imports)
        return bio.getvalue()


def pickle_decode(by: bytes) -> any:
    """
    Decode pickle bytes to object
    """
    with io.BytesIO(by) as bio:
        return pickle.load(bio)


def ensure_dir(path: Path | str) -> Path:
    """
    Ensure that the directory exists (and create if not)

    :returns The directory
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_parent(path: Path | str) -> Path:
    """
    Ensure that the parent directory of a path exists (and create if not)

    :return: The directory
    """
    path = Path(path)
    ensure_dir(path.parent)
    return path


def write(fp: Path | str, data: bytes | str, encoding: str = 'utf-8'):
    """
    Make sure the directory exists, and then write data, either in bytes or string.

    Also forces utf-8 encoding for strings.
    """
    fp = ensure_parent(fp)

    if isinstance(data, str):
        return fp.write_text(data, encoding)
    if isinstance(data, bytes):
        return fp.write_bytes(data)
