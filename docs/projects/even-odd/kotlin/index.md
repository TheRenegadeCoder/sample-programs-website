---
authors:
- Blake.Ke
- mikenmo
date: 2020-10-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- even-odd
- kotlin
title: Even Odd in Kotlin
---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].toIntOrNull() == null) {
        println("Usage: please input a number")
        return
    }
    val num = args[0].toInt()
    if (num % 2 == 0) {
        println("Even")
    } else {
        println("Odd")
    }
}
```

{% endraw %}

Even Odd in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- mikenmo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).