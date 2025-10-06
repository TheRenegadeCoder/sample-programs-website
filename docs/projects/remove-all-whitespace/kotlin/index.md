---
authors:
- Jeremy Grifski
date: 2025-10-06
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-10-06
layout: default
tags:
- kotlin
- remove-all-whitespace
title: Remove All Whitespace in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/kotlin/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import kotlin.system.exitProcess

fun main(args: Array<String>) {
    val phrase: String = errorChecking(args)
    println(removeWhitespace(phrase))
}

fun usageError() {
    println("Usage: please provide a string")
}

fun errorChecking(args: Array<String>): String {
    if (args.size == 0 || args[0] == "") {
       usageError()
       exitProcess(1)
    }
    return args[0]
}

fun removeWhitespace(phrase: String): String {
    return phrase.filter { !it.isWhitespace() }
}

```

{% endraw %}

Remove All Whitespace in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).