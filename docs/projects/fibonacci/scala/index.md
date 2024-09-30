---
authors:
- rzuckerm
date: 2023-05-15
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- fibonacci
- scala
title: Fibonacci in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/scala/how-to-implement-the-solution.md
- sources/programs/fibonacci/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.util.{Try, Success, Failure}

object Fibonacci {

  def fibonacci(n: Int) = {
    var a = 0
    var b = 1
    for (i <- 1 to n) {
      println(s"$i: $b")
      val c = a + b
      a = b
      b = c
    }
  }


  def main(args: Array[String]) = {
    Try(args(0).toInt) match {
      case Failure(_) => println("Usage: please input the count of fibonacci numbers to output")
      case Success(n) => fibonacci(n)
    }
  }
}

```

{% endraw %}

Fibonacci in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).