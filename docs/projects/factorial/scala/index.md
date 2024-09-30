---
authors:
- rzuckerm
date: 2023-05-15
featured-image: factorial-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- factorial
- scala
title: Factorial in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/scala/how-to-implement-the-solution.md
- sources/programs/factorial/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
// Scala Program to calculate 
// Factorial of a number 

import scala.util.Try

// Creating object 
object Factorial 
{ 
  // Iterative way to calculate
  // factorial
  def factorial(n: Int): Int = { 
    var f = 1
    for(i <- 1 to n) 
    { 
        f = f * i; 
    } 

    return f 
  } 

  // Driver Code 
  def main(args: Array[String]) 
  {
    val m = Try(args(0).toInt).getOrElse(-1)
    if (m < 0) {
      println("Usage: please input a non-negative integer")
    }
    else {
      println(factorial(m))
    }
  } 
} 

```

{% endraw %}

Factorial in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).