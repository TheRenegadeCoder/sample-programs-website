---
title: Bubble Sort in Scala
layout: default
date: 2019-03-22
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-03-22

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.reflect.ClassTag

object BubbleSort {
  def main(args: Array[String]) {
    // verify inputs are being provided
    parseInput(args) match {
      case None => println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
      case Some(inputArr) => {
        if (inputArr.length < 2) {
          println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
        }
        else {
          val output = bubbleSort(inputArr).mkString(", ")
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

  // bubble the current element

  // bubble sort increasing elements
  // note on signature:
  // ClassTag elements help construct Array quen using ++ (instead of falling back to ArraySeq)
  // Elements of array implement Ordered, so we can compare 2 instances of T using ==, <, >, etc.
  def bubbleSort[T <% Ordered[T]: ClassTag](arr: Array[T]): Array[T] = {
    def bubble(a: Array[T]): Array[T] = a.length match {
      case 0 => a
      case 1 => a
      case _ => {
        if (a(0) > a(1)) {
          a.slice(1, 2) ++ bubble(a.slice(0, 1) ++ a.slice(2, a.length))
        }
        else {
          a.slice(0, 1) ++ bubble(a.slice(1, a.length))
        }
      }
    }
    arr.foldLeft(arr)((xs: Array[T], cur: T) => bubble(xs))
  }
}
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Vee Ng
- Viet Thang Nguyen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 16:11:44. The solution was first committed on Mar 22 2019 12:56:04. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).