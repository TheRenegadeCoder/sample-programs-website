---
authors:
- Marius
- Ștefan-Iulian Alecu
date: 2018-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- fibonacci
title: Fibonacci in C#
title1: Fibonacci
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/c-sharp/how-to-implement-the-solution.md
- sources/programs/fibonacci/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input] || !int.TryParse(input, out int n) || n < 0)
{
    Console.Error.WriteLine("Usage: please input the count of fibonacci numbers to output");
    return;
}

int a = 1, b = 1;

for (int i = 1; i <= n; i++)
{
    Console.WriteLine($"{i}: {a}");
    (a, b) = (b, a + b);
}
```

{% endraw %}

Fibonacci in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Marius
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).