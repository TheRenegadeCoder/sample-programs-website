---
authors:
- Chris Thomas
date: 2018-10-12
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-12
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
object FizzBuzz {

  def main(args: Array[String]): Unit = {
    for (i <- 1.until(101)) {
      var output: String = ""
      if (i % 3 == 0) {
        output += "Fizz"
      }
      if (i % 5 == 0) {
        output += "Buzz"
      }
      if (output.isEmpty) {
        output += i
      }
      println(output)
    }
  }

}
```

{% endraw %}

Fizz Buzz in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Chris Thomas

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).