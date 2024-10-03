---
authors:
- rzuckerm
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- baklava
- scala
title: Baklava in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/scala/how-to-implement-the-solution.md
- sources/programs/baklava/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.math.abs

object Baklava {
  def main(args: Array[String]): Unit = {
    for (i <- -10.until(11)) {
        var numSpaces = abs(i)
        println(" " * numSpaces + "*" * (21 - 2 * numSpaces))
    }
  }
}

```

{% endraw %}

Baklava in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).