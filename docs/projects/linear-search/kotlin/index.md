---
authors:
- Matthew Larsen
date: 2025-02-13
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-02-13
layout: default
tags:
- kotlin
- linear-search
title: Linear Search in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/kotlin/how-to-implement-the-solution.md
- sources/programs/linear-search/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>)  
{
    // store usage message in variable
    val message = "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"
       
    // validate input array is correct size and does not contain empty Strings 
    if(args.size !=2 || args[0].isBlank() || args[1].isBlank())
    {
        println(message)
        return
    } 
    
    // convert input number String into a List of integers, invalid characters are converted to null
    val intList = args[0].split(",").map { it.trim().toIntOrNull() }
 
    // convert input key String into an int, invalid characters are converted to null
    val key = args[1].toIntOrNull()
 
    // check if the List or the key contains null (invalid) elements
    if(null in intList || key == null)
    {
        println(message)
        return
    }

    // check if key is in the List and print returned boolean   
    println(key in intList)
}
```

{% endraw %}

Linear Search in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Matthew Larsen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).