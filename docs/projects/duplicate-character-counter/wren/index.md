---
authors:
- Zia
date: 2025-02-17
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-02-17
layout: default
tags:
- duplicate-character-counter
- wren
title: Duplicate Character Counter in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/wren/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments

if (args.count != 1 || args[0] == "") {
  System.print("Usage: please provide a string")
  Fiber.suspend()
}

var chars = {}
var order = []
var dupes = false

for (c in args[0]) {
  if (chars[c] == null) {
    chars[c] = 0
  } else {
    dupes = true
  }

  chars[c] = chars[c] + 1

  var contains = false
  for (a in order) {
    if (c == a) {
      contains = true
      break
    }
  }

  if (!contains) {
    order.add(c)
  }
}

if (dupes) {
  for (c in order) {
    if (chars[c] > 1) {
      System.print(c + ": " + chars[c].toString)
    }
  }
} else {
  System.print("No duplicate characters")
}

```

{% endraw %}

Duplicate Character Counter in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).