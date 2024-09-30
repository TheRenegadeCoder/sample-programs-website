---
authors:
- Jeremy Grifski
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2023-04-06
layout: default
tags:
- baklava
- c-sharp
title: Baklava in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c-sharp/how-to-implement-the-solution.md
- sources/programs/baklava/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

class CSharp
{

    static void Main (string[] args)
    {

        for (SByte i = 0; i < 10; i++)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

        for (SByte i = 10; -1 < i; i--)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

    }

}

```

{% endraw %}

Baklava in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).