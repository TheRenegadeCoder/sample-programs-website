---
authors:
- konradkelly
date: 2025-10-31
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- linear-search
- scala
title: Linear Search in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/scala/how-to-implement-the-solution.md
- sources/programs/linear-search/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object LinearSearch {
    def main(args: Array[String]): Unit = {
        if (args.length != 2) {
            println("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
            return
        }
        
        val list = args(0);
        val key = args(1);

        try {
            val arr = list.split(",").map(_.trim.toInt)
            val target = key.trim.toInt
           
            var flag = 0
            var pos = -1
            for (i <- arr.indices) {
                if (arr(i) == target) {
                    flag = 1
                    pos = i
                    println("true")
                    return
                }
            }
            if (flag == 0) {
                println("false")
            }
        } catch {
            case _: NumberFormatException =>
            println("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
        }
    }
}
```

{% endraw %}

Linear Search in [Scala](https://sampleprograms.io/languages/scala) was written by:

- konradkelly

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).