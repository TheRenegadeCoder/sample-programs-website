# Fibonacci in Scala

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Scala
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.