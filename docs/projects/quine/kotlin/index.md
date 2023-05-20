---
title: Quine in Kotlin
layout: default
date: 2019-10-19
featured-image: quine-in-every-language.jpg
last-modified: 2019-10-19

---

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) { //Prints out it's own code
    val s = """fun main(args: Array<String>) { //Prints out it's own code
    val s = """

    val a = """^s\"\"\"^s\"\"\"\n\n\tval a = \"\"\"^a\"\"\"\n\tprint(\"^{a.replace(']' + 1, '$')}\")\n}\n"""
    print("$s\"\"\"$s\"\"\"\n\n\tval a = \"\"\"$a\"\"\"\n\tprint(\"${a.replace(']' + 1, '$')}\")\n}\n")
}
```

{% endraw %}

[Quine](https://sampleprograms.io/projects/quine) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).