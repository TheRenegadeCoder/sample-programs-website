---
authors:
- rzuckerm
- "\u0218tefan-Iulian Alecu"
date: 2023-05-15
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-04-11
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
object Fibonacci:

  private val fibs: LazyList[BigInt] =
    BigInt(1) #:: BigInt(1) #:: fibs.zip(fibs.tail).map(_ + _)
    
  private val usage =
    "Usage: please input the count of fibonacci numbers to output"

  def main(args: Array[String]): Unit =
    val output =
      for
        arg <- args.headOption
        n <- arg.toIntOption if n >= 0
      yield
        if n == 0 then ""
        else
          fibs
            .take(n)
            .zipWithIndex
            .map((f, i) => s"${i + 1}: $f")
            .mkString("\n")

    println(output.getOrElse(usage))
```

{% endraw %}

Fibonacci in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).