---
title: Factorial in Groovy
layout: default
date: 2019-10-12
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-12

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class Factorial {
    static def factorial(BigInteger n) {
        if (n == 0) {
            return 1
        }
        return n * factorial(n - 1)
    }

    static void main(args){
        if(args?.size() != 1 || !args[0].isInteger() || args[0].toInteger() < 0) {
          println "Usage: please input a non-negative integer"
          return
        }

        if(args[0].toInteger() >= 1000){
            println "Usage: please input a value below 1000"
            return
        }

        println factorial(args[0].toInteger())
    }
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- Rafael Vargas

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).