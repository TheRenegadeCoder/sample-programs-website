---

title: Reverse String in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-05-18


---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>){
  // Get input, or use default value
  val targetValue = when (args.size > 0 && !args[0].isNullOrBlank()) {
    true -> args[0]
    false -> throw Error("No String Provided. Nothing to Reverse")
  }  
  
  // Kotlin provides a simple `reversed()` function in the standard
  // library for all String/CharSequence objects
  println(targetValue.reversed())
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Barry Rowe

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).