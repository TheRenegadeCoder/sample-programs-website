---
authors:
- Blake.Ke
- Saurabh
date: 2019-10-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-08
layout: default
tags:
- capitalize
- kotlin
title: Capitalize in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/kotlin/how-to-implement-the-solution.md
- sources/programs/capitalize/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].isBlank()) {
        println("Usage: please provide a string")
    } else {
        // Kotlin provides a simple `capitalize()` function in the standard
        // library for all String objects
        println(args[0].capitalize())
    }
}

```

{% endraw %}

Capitalize in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Saurabh

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).