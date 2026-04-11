---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-11
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-04-11
layout: default
tags:
- fizz-buzz
- scala
title: Fizz Buzz in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/scala/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object FizzBuzz:
  def main(args: Array[String]): Unit =
    (1 to 100).map { i =>
      (i % 3, i % 5) match
        case (0, 0) => "FizzBuzz"
        case (0, _) => "Fizz"
        case (_, 0) => "Buzz"
        case _ => i.toString
    } foreach println
```

{% endraw %}

Fizz Buzz in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).