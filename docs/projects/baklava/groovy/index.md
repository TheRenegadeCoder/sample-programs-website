---
authors:
- Rafael Vargas
- rzuckerm
date: 2019-10-12
featured-image: baklava-in-every-language.jpg
last-modified: 2023-07-25
layout: default
tags:
- baklava
- groovy
title: Baklava in Groovy
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/groovy/how-to-implement-the-solution.md
- sources/programs/baklava/groovy/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
(0..10).each{ index ->
    println "${' ' * (10 - index)}${'*' * (index * 2 + 1)}"
}
(9..0).each{ index ->
    println "${' ' * (10 - index)}${'*' * (index * 2 + 1)}"
}
```

{% endraw %}

Baklava in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- Rafael Vargas
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).