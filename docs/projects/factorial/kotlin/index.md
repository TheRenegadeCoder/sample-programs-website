---
authors:
- Blake.Ke
- Satyajit Pradhan
date: 2019-10-06
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- factorial
- kotlin
title: Factorial in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/kotlin/how-to-implement-the-solution.md
- sources/programs/factorial/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import java.math.BigInteger

fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].toIntOrNull()?.takeIf { it >= 0 } == null) {
        println("Usage: please input a non-negative integer")
        return
    }

    val num = args[0].toInt()
    var factorial = BigInteger.ONE
    for (i in 1..num) {
        // factorial = factorial * i;
        factorial = factorial.multiply(BigInteger.valueOf(i.toLong()))
    }
    println(factorial)
}
```

{% endraw %}

Factorial in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Satyajit Pradhan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).