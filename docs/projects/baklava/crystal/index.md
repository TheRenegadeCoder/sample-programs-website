---
authors:
- Jeremy Grifski
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17
layout: default
tags:
- baklava
- crystal
title: Baklava in Crystal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/crystal/how-to-implement-the-solution.md
- sources/programs/baklava/crystal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Crystal](https://sampleprograms.io/languages/crystal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```crystal
a = -1
loop do
  a += 1
  puts ((" " * (10 - a)) + ("*" * (a * 2 + 1)))
  break if a == 10
end

b = 10
loop do
  b -= 1
  puts ((" " * (10 - b)) + ("*" * (b * 2 + 1)))
  break if b == 0
end

```

{% endraw %}

Baklava in [Crystal](https://sampleprograms.io/languages/crystal) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).