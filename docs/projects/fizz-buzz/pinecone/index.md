---
authors:
- rzuckerm
date: 2024-12-02
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-12-02
layout: default
tags:
- fizz-buzz
- pinecone
title: Fizz Buzz in Pinecone
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/pinecone/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/pinecone/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pinecone](https://sampleprograms.io/languages/pinecone) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pinecone
i: 1 | i <= 100 | i: i + 1 @ (
    i % 15 = 0 ? (
        print: "FizzBuzz"
    ) |
    i % 3 = 0 ? (
        print: "Fizz"
    ) |
    i % 5 = 0 ? (
        print: "Buzz"
    ) | (
        print: i
    )
)

```

{% endraw %}

Fizz Buzz in [Pinecone](https://sampleprograms.io/languages/pinecone) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).