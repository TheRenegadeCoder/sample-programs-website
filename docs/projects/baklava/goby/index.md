---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- goby
title: Baklava in Goby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/goby/how-to-implement-the-solution.md
- sources/programs/baklava/goby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Goby](https://sampleprograms.io/languages/goby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```goby
(-10..10).each do |n|
    num_spaces = if n >= 0 n else -n end
    num_stars = 21 - 2 * num_spaces
    puts(" " * num_spaces + "*" * num_stars)
end

```

{% endraw %}

Baklava in [Goby](https://sampleprograms.io/languages/goby) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).