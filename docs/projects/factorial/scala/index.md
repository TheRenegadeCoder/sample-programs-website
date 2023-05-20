---
title: Factorial in Scala
layout: default
date: 2023-05-15
featured-image: factorial-in-every-language.jpg
last-modified: 2023-05-15

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
// Scala Program to calculate 
// Factorial of a number 

import scala.util.Try

// Creating object 
object Factorial 
{ 
  // Iterative way to calculate
  // factorial
  def factorial(n: Int): Int = { 
    var f = 1
    for(i <- 1 to n) 
    { 
        f = f * i; 
    } 

    return f 
  } 

  // Driver Code 
  def main(args: Array[String]) 
  {
    val m = Try(args(0).toInt).getOrElse(-1)
    if (m < 0) {
      println("Usage: please input a non-negative integer")
    }
    else {
      println(factorial(m))
    }
  } 
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).