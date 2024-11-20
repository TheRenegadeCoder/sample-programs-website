---
authors:
- rzuckerm
date: 2024-11-20
featured-image: baklava-in-every-language.jpg
last-modified: 2024-11-20
layout: default
tags:
- baklava
- pineapple
title: Baklava in Pineapple
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/pineapple/how-to-implement-the-solution.md
- sources/programs/baklava/pineapple/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Pineapple](https://sampleprograms.io/languages/pineapple) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pineapple
def (this String).repeat(times Number) -> String
    let i mutable = times
    let s mutable = ""
    while i > 0
        s =  "$(s)$(this)"
        i = i - 1

    return s

def .main
    let i mutable = -10
    while i <= 10
        let numSpaces mutable = i
        if numSpaces < 0
            numSpaces = -numSpaces

        let spaces = " ".repeat(numSpaces)
        let stars = "*".repeat(21 - (2 * numSpaces))
        "$(spaces)$(stars)".show
        i = i + 1

```

{% endraw %}

Baklava in [Pineapple](https://sampleprograms.io/languages/pineapple) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).