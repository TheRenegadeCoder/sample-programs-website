---
authors:
- Cristiano Lopes
- Jeremy Grifski
date: 2020-10-07
featured-image: rot13-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- kotlin
- rot13
title: Rot13 in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/kotlin/how-to-implement-the-solution.md
- sources/programs/rot13/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
data class EncodingBounds(val lowerBound: Int, val upperBound: Int)

fun encodingBoundsForCharValue(c: Char): EncodingBounds? {
    val lowerCaseBounds = EncodingBounds('a'.toInt(), 'z'.toInt())
    val upperCaseBounds = EncodingBounds('A'.toInt(), 'Z'.toInt())
    return when (c) {
        in 'a'..'z' -> lowerCaseBounds
        in 'A'..'Z' -> upperCaseBounds
        else -> null
    }
}

fun calculateRotatedChar(char: Char, rotation: Int, bounds: EncodingBounds): Char {
    val rotatedCharVal = char.toInt() + rotation
    val remainder = rotatedCharVal - (bounds.upperBound + 1)
    return (if (rotatedCharVal > bounds.upperBound) bounds.lowerBound + remainder else rotatedCharVal).toChar()
}

fun parseInput(args: Array<String>): String? {
    if (args.isEmpty()) {
        return null
    }
    val text = args[0]
    if (text.isEmpty()) {
        return null
    }
    return text
}

fun rot13Encode(text: String): String {
    val rotation = 13

    return text.map { c ->
        val bounds = encodingBoundsForCharValue(c)
        if (bounds == null) {
            c.toString()
        } else {
            calculateRotatedChar(c, rotation, bounds).toString()
        }
    }.reduce { encodedText, encodedChar ->
        encodedText + encodedChar
    }

}

fun main(args: Array<String>) {
    val strToEncode = parseInput(args)
    if (strToEncode == null) {
        println("Usage: please provide a string to encrypt")
    } else {
        println(rot13Encode(strToEncode))
    }
}

```

{% endraw %}

Rot13 in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Cristiano Lopes
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).