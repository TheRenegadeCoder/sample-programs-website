---
title: Duplicate Character Counter in Python
layout: default
date: 2022-05-14
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2022-05-14

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

if len(sys.argv) != 2 or not sys.argv[1]:
    print("Usage: please provide a string")
    sys.exit()

counter = dict()
dupes = False
for char in sys.argv[1]:
    counter.setdefault(char, 0)
    counter[char] += 1
    if counter[char] > 1:
        dupes = True

if dupes:
    for key, value in counter.items():
        if value > 1:
            print(f"{key}: {value}")
else:
    print("No duplicate characters")
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).