---
authors:
- f3liz
- Ștefan-Iulian Alecu
date: 2024-11-08
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- longest-word
title: Longest Word in C#
title1: Longest
title2: Word in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-word/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var sentence] || string.IsNullOrWhiteSpace(sentence))
    return Usage();

int max = 0,
    cur = 0;

foreach (char c in sentence)
{
    if (char.IsWhiteSpace(c))
    {
        cur = 0;
        continue;
    }

    cur++;
    max = Math.Max(cur, max);
}

Console.WriteLine(max);
return 0;

static int Usage()
{
    Console.Error.WriteLine("Usage: please provide a string");
    return 1;
}

```

{% endraw %}

Longest Word in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- f3liz
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).