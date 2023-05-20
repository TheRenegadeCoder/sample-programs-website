---
title: Fibonacci in Kotlin
layout: default
date: 2018-10-18
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-18

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import kotlin.system.exitProcess

// First arg is number of iterations to run
fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].toIntOrNull()?.takeIf { it >= 0 } == null) {
        println("Usage: please input the count of fibonacci numbers to output")
        return
    }

    val iterations = args[0].toInt()

    var j: Int
    var k = 0
    var l = 1

    for (i in 1..iterations) {
        println("$i: $l")

        j = k
        k = l
        l = j + k
    }
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Erik Nelson

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:34:00. The solution was first committed on Oct 18 2018 14:52:56. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).