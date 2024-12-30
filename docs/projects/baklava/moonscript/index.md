---
authors:
- rzuckerm
date: 2024-12-30
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-30
layout: default
tags:
- baklava
- moonscript
title: Baklava in Moonscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/moonscript/how-to-implement-the-solution.md
- sources/programs/baklava/moonscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Moonscript](https://sampleprograms.io/languages/moonscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```moonscript
string_repeat = (s, n) ->
  result = ""
  for i = 1, n
    result ..= s
  return result

for i = -10, 10
  num_spaces = math.abs i
  num_stars = 21 - 2 * num_spaces
  print string_repeat(" ", num_spaces) .. string_repeat("*", num_stars)

```

{% endraw %}

Baklava in [Moonscript](https://sampleprograms.io/languages/moonscript) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).