---
authors:
- Huma Homidov
- Ștefan-Iulian Alecu
date: 2024-11-12
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- duplicate-character-counter
title: Duplicate Character Counter in C#
title1: Duplicate Character
title2: Counter in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/c-sharp/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input] || string.IsNullOrWhiteSpace(input))
{
    Console.Error.WriteLine("Usage: please provide a string");
    return;
}

Span<int> freq = stackalloc int[128];

foreach (char c in input)
    if (c < 128)
        freq[c]++;

bool found = false;

foreach (char c in input)
{
    if (c >= 128 || freq[c] < 2)
        continue;

    Console.WriteLine($"{c}: {freq[c]}");
    freq[c] = 0;
    found = true;
}

if (!found)
    Console.WriteLine("No duplicate characters");
```

{% endraw %}

Duplicate Character Counter in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Huma Homidov
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).