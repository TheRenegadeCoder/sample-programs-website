---
title: Fizz Buzz in Scala
layout: default
date: 2018-10-12
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-12

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Chris Thomas

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).