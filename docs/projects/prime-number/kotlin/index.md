---
authors:
- Blake.Ke
- smallblack9
date: 2020-10-08
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- kotlin
- prime-number
title: Prime Number in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/kotlin/how-to-implement-the-solution.md
- sources/programs/prime-number/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) 
{
    if (args.isNullOrEmpty() || args[0].isBlank() || args[0].toIntOrNull()?.takeIf { it >= 0 } == null) {
        println("Usage: please input a non-negative integer")
        return
    }

    val num = args[0].toInt()
    if(num>1)
    {
        for(i in 2 until num)
        {
            if(num%i == 0)
            {
                println("Composite")
                return
            }
        }
        println("Prime")
    }
    else
    {
        println("Composite")
    }
}

```

{% endraw %}

Prime Number in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).