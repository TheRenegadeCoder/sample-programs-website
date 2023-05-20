---
title: Capitalize in Scala
layout: default
date: 2023-05-15
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-05-15

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object Capitalize {
  def main(args: Array[String]) {
    val inputStr: Option[String] = args.length match {
      case 0 => Some("")
      case _ => Some(args(0))
    }
    if (inputStr.get.length < 1) {
      println("Usage: please provide a string")
    }
    else {
      inputStr.map(_.capitalize).map(println)
    }
  }
}
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).