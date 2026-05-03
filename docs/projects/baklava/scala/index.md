---
authors:
- rzuckerm
- Ștefan-Iulian Alecu
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- baklava
- scala
title: Baklava in Scala
title1: Baklava
title2: in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/scala/how-to-implement-the-solution.md
- sources/programs/baklava/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object Baklava:
  def generate(size: Int): Seq[String] =
    for i <- -size to size yield
      val spaces = i.abs
      val stars = (size * 2 + 1) - 2 * spaces
      " " * spaces + "*" * stars

  def main(args: Array[String]): Unit =
    val size =
      if args.nonEmpty then args(0).toInt
      else 10

    generate(size).foreach(println)
```

{% endraw %}

Baklava in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).