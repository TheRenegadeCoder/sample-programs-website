---
authors:
- rzuckerm
date: 2024-10-19
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-19
layout: default
tags:
- baklava
- raku
title: Baklava in Raku
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/raku/how-to-implement-the-solution.md
- sources/programs/baklava/raku/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Raku](https://sampleprograms.io/languages/raku) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```raku
for -10 .. 10 {
    my $numSpaces = $_.abs;
    say (" " x $numSpaces) ~ ("*" x (21 - 2 * $numSpaces));
}

```

{% endraw %}

Baklava in [Raku](https://sampleprograms.io/languages/raku) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).