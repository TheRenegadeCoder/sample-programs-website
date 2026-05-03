---
authors:
- rzuckerm
- Ștefan-Iulian Alecu
date: 2023-05-15
featured-image: factorial-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- factorial
- scala
title: Factorial in Scala
title1: Factorial
title2: in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/scala/how-to-implement-the-solution.md
- sources/programs/factorial/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.util.Try

object Factorial:
  private val usage = "Usage: please input a non-negative integer"

  def main(args: Array[String]): Unit =
    val result =
      args.headOption
        .flatMap(a => Try(a.toInt).toOption)
        .filter(_ >= 0)
        .map(factorial)

    result match
      case Some(value) => println(value)
      case None => println(usage)

  private def factorial(n: Int): Int =
    (1 to n).product
```

{% endraw %}

Factorial in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).