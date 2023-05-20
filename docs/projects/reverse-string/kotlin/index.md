---
title: Reverse String in Kotlin
layout: default
date: 2018-10-20
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-10-20

---

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

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Barry Rowe
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 20 2018 12:01:39. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).