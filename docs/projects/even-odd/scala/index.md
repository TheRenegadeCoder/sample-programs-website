---
title: Even Odd in Scala
layout: default
date: 2023-05-15
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-05-15

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
// Scala Program to check if input number is Odd or Even

import scala.util.{Try, Success, Failure}

object EvenOdd 
{
    def check_even_odd(num: Int): String = { 
        val result = if (num%2==0) "Even" else "Odd"
        return result
    }

    // Driver Code 
    def main(args: Array[String]) 
    {
        Try(args(0).toInt) match {
            case Failure(_) => println("Usage: please input a number")
            case Success(m) => println(check_even_odd(m))
        }
    }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).