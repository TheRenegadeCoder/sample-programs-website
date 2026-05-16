---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-28
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- even-odd
title: Even Odd in C#
title1: Even Odd
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/c-sharp/how-to-implement-the-solution.md
- sources/programs/even-odd/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input] || !int.TryParse(input, out int n))
{
    Console.Error.WriteLine("Usage: please input a number");
    return;
}

Console.WriteLine(n % 2 == 0 ? "Even" : "Odd");
```

{% endraw %}

Even Odd in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).