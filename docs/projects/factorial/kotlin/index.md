---
title: Factorial in Kotlin
layout: default
date: 2019-10-06
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-06

---

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

[Factorial](https://sampleprograms.io/projects/factorial) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Satyajit Pradhan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:34:00. The solution was first committed on Oct 06 2019 08:53:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).