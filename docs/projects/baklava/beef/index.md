---
authors:
- rzuckerm
date: 2024-01-14
featured-image: baklava-in-every-language.jpg
last-modified: 2024-01-14
layout: default
tags:
- baklava
- beef
title: Baklava in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/beef/how-to-implement-the-solution.md
- sources/programs/baklava/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace Baklava;

class Program
{
    public static int Main(String[] args)
    {
        for (int i in -10...10)
        {
            int num_spaces = Math.Abs(i);
            int num_stars = 21 - 2 * num_spaces;
            String line = scope String();
            line.Append(' ', num_spaces);
            line.Append('*', num_stars);
            Console.WriteLine(line);
        }
        return 0;
    }
}

```

{% endraw %}

Baklava in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).