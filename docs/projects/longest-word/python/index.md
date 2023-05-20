---
title: Longest Word in Python
layout: default
date: 2022-05-13
featured-image: longest-word-in-every-language.jpg
last-modified: 2022-05-13

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

error = "Usage: please provide a string"

if len(sys.argv) == 1 or sys.argv[1] == "":
    print(error)
    sys.exit(1)

input_string = sys.argv[1]
longest_word = max(len(word) for word in input_string.split())
print(longest_word)
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).