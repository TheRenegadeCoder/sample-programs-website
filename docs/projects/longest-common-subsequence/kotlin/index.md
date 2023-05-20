---
title: Longest Common Subsequence in Kotlin
layout: default
date: 2020-10-05
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2020-10-05

---

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin

private fun lcsOf(a: MutableList<String>, b: MutableList<String>, indexA: Int, indexB: Int): MutableList<String> {
    return if (indexA < 0 || indexB < 0) {
        mutableListOf()
    } else if (a[indexA] == b[indexB]) {
        // get the best subsequence of the rest, then add this one at the end (prevents needing to reverse at the end)
        lcsOf(a, b, indexA - 1, indexB - 1).also { it.add(a[indexA] )}
    } else {
        // compare both subsequences and return the one that has more element
        val subA = lcsOf(a, b, indexA, indexB - 1)
        val subB = lcsOf(a, b, indexA - 1, indexB)
        if (subA.size >= subB.size) subA else subB
    }
}

// only require consumers to pass in the lists... we'll handle the indices ourselves
fun lcsOf(a: List<String>, b: List<String>) = lcsOf(a.toMutableList(), b.toMutableList(), a.size - 1, b.size - 1)

fun main(args: Array<String>) {
    if (args.size != 2 || args[0].isBlank() || args[1].isBlank()) {
        // print and exit if we don't have the correct number of arguments
        println("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"")
        return
    }

    // split each argument by comma, remove whitespace around each element, and pack them all in a list
    val seqA = args[0].split(",").map { it.trim() }
    val seqB = args[1].split(",").map { it.trim() }

    lcsOf(seqA, seqB).joinToString(", ").also { println(it) }
}
```

{% endraw %}

[Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- David Phillips

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:02:08. The solution was first committed on Oct 05 2020 00:20:57. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).