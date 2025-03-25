---
authors:
- Zia
date: 2025-03-25
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-25
layout: default
tags:
- base64-encode-decode
- python
title: Base64 Encode Decode in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/python/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import base64
import binascii
import sys
from typing import NoReturn


def usage() -> NoReturn:
    print("Usage: please provide a mode and a string to encode/decode")
    sys.exit(1)


def base64_encode(s: str) -> str:
    return base64.b64encode(s.encode("ascii")).decode("ascii")


def base64_decode(s: str) -> str:
    return base64.b64decode(s.encode("ascii")).decode("ascii")


def main() -> None | NoReturn:
    if len(sys.argv) < 3 or not sys.argv[2]:
        usage()

    mode = sys.argv[1]
    s = sys.argv[2]
    if mode == "encode":
        result = base64_encode(s)
    elif mode == "decode":
        try:
            result = base64_decode(s)
        except binascii.Error:
            usage()
    else:
        usage()

    print(result)


if __name__ == "__main__":
    main()

```

{% endraw %}

Base64 Encode Decode in [Python](https://sampleprograms.io/languages/python) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).