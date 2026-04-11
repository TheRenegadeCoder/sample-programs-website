---
authors:
- rzuckerm
- "\u0218tefan-Iulian Alecu"
date: 2023-05-15
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- even-odd
- scala
title: Even Odd in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/scala/how-to-implement-the-solution.md
- sources/programs/even-odd/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.util.Try

object EvenOdd:
  private val usage = "Usage: please input a number"

  def main(args: Array[String]): Unit =
    val result =
      args.headOption
        .flatMap(a => Try(a.toInt).toOption)
        .map(n => if n % 2 == 0 then "Even" else "Odd")
        .getOrElse(usage)

    println(result)
```

{% endraw %}

Even Odd in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).