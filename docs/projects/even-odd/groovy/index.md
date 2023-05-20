---
title: Even Odd in Groovy
layout: default
date: 2019-07-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-07-01

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class EvenOdd {
  static void main(String... args) {
    if(args?.length != 1 || !args[0]?.isInteger()) {
      println 'Usage: please input a number'
    } else {
      println args[0].toInteger() % 2 == 0 ? 'Even' : 'Odd'
    }
  }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- robin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).