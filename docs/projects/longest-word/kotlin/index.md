---
authors:
- mechance782
date: 2024-11-11
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-11-11
layout: default
tags:
- kotlin
- longest-word
title: Longest Word in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/kotlin/how-to-implement-the-solution.md
- sources/programs/longest-word/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) {

    fun longestWord(sentence: String): Any {
        // if sentence is empty, ask for a String
        if (sentence.length == 0){
            return "Usage: please provide a string"
        } else {
            // split sentence from these delimeters and put resulting strings into words list
            var words = sentence.split(" ", "\t", "\n", "\r")
            var longest = 0
            // iterate through words list and compare each word length to longest var
            // if word length is larger, then the var longest will be assigned the word length
            for (word in words){
                when {
                    word.length > longest -> longest = word.length
                }
            }
            // return var longest which holds the largest string length in the sentence parameter
            return longest
        }
    }    

    // if console input is null, ask for String
    if (args.isNullOrEmpty()){
        println("Usage: please provide a string")
    } else {
        // if console input is not null, then find longestWord of input String
        println(longestWord(args[0]))    
    }
    
}
```

{% endraw %}

Longest Word in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- mechance782

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).