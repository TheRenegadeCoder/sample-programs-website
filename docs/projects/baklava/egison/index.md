---
authors:
- rzuckerm
date: 2025-01-08
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-08
layout: default
tags:
- baklava
- egison
title: Baklava in Egison
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/egison/how-to-implement-the-solution.md
- sources/programs/baklava/egison/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Egison](https://sampleprograms.io/languages/egison) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```egison
def stringRepeat s n :=
    (S.concat (take n (repeat1 s)))

def baklavaLine n :=
    let numSpaces := abs (n - 10)
        numStars := 21 - 2 * numSpaces in
    (S.concat [(stringRepeat " " numSpaces), (stringRepeat "*" numStars), "\n"])

def baklava n :=
    (S.concat (map baklavaLine [0..n]))

def main args := do
    write (baklava 20)

```

{% endraw %}

Baklava in [Egison](https://sampleprograms.io/languages/egison) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).