---
authors:
- rzuckerm
date: 2024-12-27
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-27
layout: default
tags:
- baklava
- lily
title: Baklava in Lily
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/lily/how-to-implement-the-solution.md
- sources/programs/baklava/lily/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Lily](https://sampleprograms.io/languages/lily) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lily
import math

define repeatString(s: String, n: Integer): String
{
    var result = ""
    if n > 0: {
        for i in 1...n: {
            result = "{0}{1}".format(result, s)
        }
    }

    return result
}

for n in -10...10: {
    var num_spaces = math.abs(n)
    var num_stars = 21 - 2 * num_spaces
    print("{0}{1}".format(repeatString(" ", num_spaces), repeatString("*", num_stars)))
}

```

{% endraw %}

Baklava in [Lily](https://sampleprograms.io/languages/lily) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).