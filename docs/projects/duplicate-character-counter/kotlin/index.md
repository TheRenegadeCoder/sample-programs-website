---
authors:
- Jeremy Grifski
date: 2025-10-07
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-10-07
layout: default
tags:
- duplicate-character-counter
- kotlin
title: Duplicate Character Counter in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/kotlin/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import kotlin.system.exitProcess

fun main(args: Array<String>) {
    val phrase: String = errorChecking(args)
    val counts = duplicateCharacterCount(phrase)
    outputMap(counts)
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

fun duplicateCharacterCount(phrase: String): Map<Char, Int> {
    val counts: Map<Char, Int> = phrase.groupingBy { it }.eachCount()
    return counts.filter { it.value > 1 }
}

fun outputMap(counts: Map<Char, Int>) {
    if (counts.size > 0) {
        for (pair in counts) {
            println("${pair.key}: ${pair.value}")
        }
    } else {
        println("No duplicate characters")
    }
}

```

{% endraw %}

Duplicate Character Counter in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).