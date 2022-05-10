---

title: Fizz Buzz in Scala
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Fizz Buzz in Scala page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```scala
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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).