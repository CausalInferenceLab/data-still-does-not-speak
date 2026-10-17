"""Read CSVs locally and after browser HTTP decoding."""
import gzip
from io import BytesIO
from urllib.request import urlopen

import pandas as pd


def read_csv(source):
    if not str(source).startswith(("https://", "http://")):
        return pd.read_csv(source)
    with urlopen(str(source)) as response:
        body = response.read()
    # Browsers may decode gzip while retaining the Content-Encoding header.
    if body.startswith(b"\x1f\x8b"):
        body = gzip.decompress(body)
    return pd.read_csv(BytesIO(body))
