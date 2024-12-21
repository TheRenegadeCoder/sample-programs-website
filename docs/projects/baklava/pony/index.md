---
authors:
- rzuckerm
date: 2024-12-21
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-21
layout: default
tags:
- baklava
- pony
title: Baklava in Pony
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/pony/how-to-implement-the-solution.md
- sources/programs/baklava/pony/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Pony](https://sampleprograms.io/languages/pony) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pony
actor Main
  new create(env: Env) =>
    var n: I32 = -10
    while n <= 10 do
      let numSpaces: I32 = if n >= 0 then n else -n end
      let numStars: I32 = 21 - (2 * numSpaces)
      env.out.print(repeatString(" ", numSpaces) + repeatString("*", numStars))
      n = n + 1
    end

  fun repeatString(s: String, n: I32): String =>
    var result = ""
    var i: I32 = 0
    while i < n do
      result = result + s
      i = i + 1
    end
    result

```

{% endraw %}

Baklava in [Pony](https://sampleprograms.io/languages/pony) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).