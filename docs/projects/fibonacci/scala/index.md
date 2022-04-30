---

title: Fibonacci in Scala
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in Scala page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).