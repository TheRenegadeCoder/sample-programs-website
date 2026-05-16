---
authors:
- Viet Thang Nguyen
- Ștefan-Iulian Alecu
date: 2019-03-22
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- quick-sort
- scala
title: Quick Sort in Scala
title1: Quick Sort
title2: in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/scala/how-to-implement-the-solution.md
- sources/programs/quick-sort/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.util.Try

object QuickSort:

  def main(args: Array[String]): Unit =
    val input = args.headOption.getOrElse("")

    parse(input) match
      case Some(nums) if nums.length >= 2 =>
        println(sort(nums).mkString(", "))
      case _ =>
        println(usage)

  def usage: String =
    """Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5""""

  def sort(xs: List[Int]): List[Int] =
    xs match
      case Nil => Nil
      case pivot :: tail =>
        val (less, more) = tail.partition(_ < pivot)
        sort(less) ++ (pivot :: sort(more))

  def parse(input: String): Option[List[Int]] =
    Try(input.split(',').toList.map(_.trim.toInt)).toOption
```

{% endraw %}

Quick Sort in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Viet Thang Nguyen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).