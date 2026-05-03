---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- capitalize
- scala
title: Capitalize in Scala
title1: Capitalize
title2: in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/scala/how-to-implement-the-solution.md
- sources/programs/capitalize/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object Capitalize:
  def main(args: Array[String]): Unit =
    args.headOption.filter(_.nonEmpty) match
      case Some(str) => println(str.capitalize)
      case None      => println("Usage: please provide a string")
```

{% endraw %}

Capitalize in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).