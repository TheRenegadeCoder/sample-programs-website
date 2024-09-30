---
authors:
- rzuckerm
- Vee Ng
- Viet Thang Nguyen
date: 2019-03-22
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- reverse-string
- scala
title: Reverse String in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/scala/how-to-implement-the-solution.md
- sources/programs/reverse-string/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object ReverseString {
  // revese using recursive & pattern matching
  def reverseString(str: String): String = str.length match {
    case 0 => ""
    case 1 => str
    case _ => reverseString(tail(str)) ++ head(str)
  }

  def head(str: String): String = str.length match {
    case 0 => ""
    case _ => str.slice(0, 1)
  }

  def tail(str: String): String = str.length match {
    case 0 => ""
    case 1 => ""
    case _ => str.slice(1, str.length)
  }

  def main(args: Array[String]) {
    val inputStr: Option[String] = args.length match {
      case 0 => None
      case _ => Some(args(0))
    }
    inputStr.map(reverseString).map(println)
  }
}

```

{% endraw %}

Reverse String in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Vee Ng
- Viet Thang Nguyen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).