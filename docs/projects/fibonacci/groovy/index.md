---
authors:
- Loic Beylot
- rzuckerm
date: 2018-10-18
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-07-25
layout: default
tags:
- fibonacci
- groovy
title: Fibonacci in Groovy
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/groovy/how-to-implement-the-solution.md
- sources/programs/fibonacci/groovy/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class Fibonacci {
    static void main(String[] args) {
        if (args.length < 1 || !args[0].isInteger()) {
            println 'Usage: please input the count of fibonacci numbers to output'
        } else {
            def n = args[0] as Integer
            if (n > 0) {
                def first = 0G
                def second = 1G
                (1..n).each {
                    second += first
                    first = second - first
                    println "$it: $first"
                }
            }
        }
    }
}

```

{% endraw %}

Fibonacci in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- Loic Beylot
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).