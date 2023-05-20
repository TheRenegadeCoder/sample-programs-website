---
title: Fibonacci in Groovy
layout: default
date: 2018-10-18
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-18

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class Fibonacci {
    static void main(String[] args) {
        if (args.length < 1 || !args[0].isInteger()) {
            println 'please provide a positive integer'
        } else {
            def n = args[0] as Integer
            def first = 0G
            def second = 1G
            println first.class
            (1..n).each {
                second += first
                first = second - first
                println "$it: $first"
            }
        }
    }
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- Jeremy Grifski
- Loic Beylot

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 21 2018 14:29:00. The solution was first committed on Oct 18 2018 19:51:09. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).