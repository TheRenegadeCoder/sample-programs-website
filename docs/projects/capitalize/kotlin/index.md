---
title: Capitalize in Kotlin
layout: default
date: 2019-10-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-11

---

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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Saurabh

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 08 2020 22:09:00. The solution was first committed on Oct 11 2019 23:46:12. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).