---
authors:
- Barry Rowe
- rzuckerm
date: 2018-10-20
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-03-19
layout: default
tags:
- kotlin
- reverse-string
title: Reverse String in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/kotlin/how-to-implement-the-solution.md
- sources/programs/reverse-string/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>){
  // Get input, or use default value
  val targetValue = when (args.size > 0 && !args[0].isNullOrBlank()) {
    true -> args[0]
    false -> ""
  }  
  
  // Kotlin provides a simple `reversed()` function in the standard
  // library for all String/CharSequence objects
  println(targetValue.reversed())
}
```

{% endraw %}

Reverse String in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Barry Rowe
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).