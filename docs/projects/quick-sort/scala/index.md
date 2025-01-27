---
authors:
- rzuckerm
- Vee Ng
- Viet Thang Nguyen
date: 2019-03-22
featured-image: quick-sort-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- quick-sort
- scala
title: Quick Sort in Scala
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
import scala.reflect.ClassTag

object QuickSort {
  def main(args: Array[String]) {
    // verify inputs are being provided
    parseInput(args) match {
      case None => println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
      case Some(inputArr) => {
        if (inputArr.length < 2) {
          println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
        }
        else {
          val output = quicksort(inputArr).mkString(", ")
          println(output)
        }
      }
    }
  }

  def parseInput(args: Array[String]): Option[Array[Int]] = args.length match {
    case 0 => None
    case _ => try {
      Some(args(0).split(",").map(_.trim).map(_.toInt))
    } catch {
      case e: Throwable => None
    }
  }

  // quick sort increasing elements
  // note on signature:
  // ClassTag elements help construct Array quen using ++ (instead of falling back to ArraySeq)
  // Elements of array implement Ordered, so we can compare 2 instances of T using ==, <, >, etc.
  def quicksort[T <% Ordered[T]: ClassTag](arr: Array[T]): Array[T] = arr.length match {
    case 0 => arr
    case 1 => arr
    case _ => {
      val pivot: T = arr(0)
      val lhs = arr.filter(_ < pivot)
      val mid = arr.filter(_ == pivot)
      val rhs = arr.filter(_ > pivot)

      quicksort(lhs) ++ mid ++ quicksort(rhs)
    }
  }
}
```

{% endraw %}

Quick Sort in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Vee Ng
- Viet Thang Nguyen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).