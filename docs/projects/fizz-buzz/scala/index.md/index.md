---

---

# Fizz Buzz in Scala

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Scala
object FizzBuzz {

  def main(args: Array[String]): Unit = {
    for (i <- 1.until(101)) {
      var output: String = ""
      if (i % 3 == 0) {
        output += "Fizz"
      }
      if (i % 5 == 0) {
        output += "Buzz"
      }
      if (output.isEmpty) {
        output += i
      }
      println(output)
    }
  }

}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.