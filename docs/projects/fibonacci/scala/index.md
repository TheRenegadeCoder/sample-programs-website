---

title: Fibonacci in Scala
layout: default
date: 2022-04-28
last-modified: 2022-08-21

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import javax.xml.bind.ValidationException

object TestClass {

  def fibonacci_rec(n: Int): Int = {
    if (n < 0) {
      // If invalid input throw an exception
      throw new ValidationException("Index should be positive")

    } else if (n == 1 || n == 2) {
      // Recursion anchors

      return 1

    } else {
      // Definition of Fibonacci sequence (sum of two previous numbers in the sequence)

      return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    }

  }


  def main(args: Array[String]): Unit = {
    // Takes the first argument and uses it as index
    if (args.length == 0) {
      println("Please enter an index as an argument")
    }
    val index = args(0).toInt
    println(fibonacci_rec(index))
  }
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- paul-you

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 27 2019 19:46:35. The solution was first committed on Oct 25 2019 15:33:55. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).