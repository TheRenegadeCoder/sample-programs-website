---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-11
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- bubble-sort
- scala
title: Bubble Sort in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/scala/how-to-implement-the-solution.md
- sources/programs/bubble-sort/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.annotation.tailrec
import scala.math.Ordering.Implicits.infixOrderingOps

object BubbleSort:

  private val usage =
    """Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5""""

  def main(args: Array[String]): Unit =
    val result =
      args.headOption
        .flatMap(parse)
        .map(bubbleSort)
        .map(_.mkString(", "))
        .getOrElse(usage)

    println(result)

  private def parse(input: String): Option[List[Int]] =
    val parts = input.split(',').map(_.trim).toList
    val nums = parts.flatMap(_.toIntOption)
    Option.when(nums.size >= 2 && nums.size == parts.size)(nums)

  private def bubbleSort[T: Ordering](xs: List[T]): List[T] =
    @tailrec
    def pass(list: List[T], acc: List[T] = Nil, swapped: Boolean = false): (List[T], Boolean) =
      list match
        case a :: b :: tail if a > b =>
          pass(a :: tail, b :: acc, true)
        case a :: tail =>
          pass(tail, a :: acc, swapped)
        case Nil =>
          (acc.reverse, swapped)

    @tailrec
    def loop(current: List[T]): List[T] =
      val (next, swapped) = pass(current)
      if swapped then loop(next)
      else next

    loop(xs)
```

{% endraw %}

Bubble Sort in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).