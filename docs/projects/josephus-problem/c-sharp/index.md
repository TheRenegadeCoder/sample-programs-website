---
authors:
- Ben Mojo
- Ștefan-Iulian Alecu
date: 2024-11-06
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- josephus-problem
title: Josephus Problem in C#
title1: Josephus
title2: Problem in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/c-sharp/how-to-implement-the-solution.md
- sources/programs/josephus-problem/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (
    args is not [var nText, var kText]
    || !int.TryParse(nText, out int n)
    || !int.TryParse(kText, out int k)
    || n <= 0
    || k <= 0
)
{
    Console.Error.WriteLine(
        "Usage: please input the total number of people and number of people to skip."
    );
    return;
}

int survivor = 0;
for (int i = 2; i <= n; i++)
    survivor = (survivor + k) % i;

Console.WriteLine(survivor + 1);

```

{% endraw %}

Josephus Problem in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ben Mojo
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).