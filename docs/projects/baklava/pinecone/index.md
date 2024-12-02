---
authors:
- rzuckerm
date: 2024-12-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-02
layout: default
tags:
- baklava
- pinecone
title: Baklava in Pinecone
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/pinecone/how-to-implement-the-solution.md
- sources/programs/baklava/pinecone/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Pinecone](https://sampleprograms.io/languages/pinecone) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pinecone
repeatStr :: {n: Int, c: String} -> {String}: (
    s: ""
    i: 0 | i < in.n | i: i + 1 @ (
        s: s + in.c
    )

    s
)

i: 0 - 10 | i <= 10 | i: i + 1 @ (
    numSpaces: i
    i < 0 ? (
        numSpaces: 0 - i
    )
    print: (repeatStr: numSpaces, " ") + (repeatStr: 21 - 2 * numSpaces, "*")
)

```

{% endraw %}

Baklava in [Pinecone](https://sampleprograms.io/languages/pinecone) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).