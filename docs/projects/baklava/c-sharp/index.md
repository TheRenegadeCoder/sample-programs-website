---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- baklava
- c-sharp
title: Baklava in C#
title1: Baklava
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c-sharp/how-to-implement-the-solution.md
- sources/programs/baklava/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
const int Height = 10;
const char Symbol = '*';

Span<char> stars = stackalloc char[Height * 2 + 1];
stars.Fill(Symbol);

static void PrintRow(int level, int height, ReadOnlySpan<char> stars)
{
    Console.Write(new string(' ', height - level));
    Console.WriteLine(stars[..(level * 2 + 1)]);
}

for (int i = 0; i < Height; i++)
    PrintRow(i, Height, stars);

for (int i = Height; i >= 0; i--)
    PrintRow(i, Height, stars);

```

{% endraw %}

Baklava in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).