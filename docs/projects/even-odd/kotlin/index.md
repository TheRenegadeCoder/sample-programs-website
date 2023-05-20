---
title: Even Odd in Kotlin
layout: default
date: 2020-10-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-01

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

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- mikenmo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:34:00. The solution was first committed on Oct 01 2020 15:03:47. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).