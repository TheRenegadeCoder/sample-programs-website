---
authors:
- konradkelly
- "\u0218tefan-Iulian Alecu"
date: 2025-10-31
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- linear-search
- scala
title: Linear Search in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/scala/how-to-implement-the-solution.md
- sources/programs/linear-search/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.util.Try

object LinearSearch:

  private val usage =
    """Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")"""

  def main(args: Array[String]): Unit =
    if args.length < 2 then
      println(usage)
    else
      val listStr = args(0)
      val targetStr = args(1)

      val output =
        for
          numbers <- parseNumbers(listStr)
          target   <- targetStr.toIntOption
        yield numbers.contains(target)

      println(output.map(_.toString).getOrElse(usage))

  private def parseNumbers(input: String): Option[List[Int]] =
    Try(input.split(',').map(_.trim.toInt).toList).toOption
```

{% endraw %}

Linear Search in [Scala](https://sampleprograms.io/languages/scala) was written by:

- konradkelly
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).