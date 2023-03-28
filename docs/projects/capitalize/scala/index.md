---

title: Capitalize in Scala
layout: default
date: 2022-04-28
last-modified: 2023-03-28

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.io.StdIn.readLine

object Capitalize {
  // Adding a method for Brevity 
  def Capitalize_String(str: String): String = str.length match {
    case 0 => ""
    case _ => str.capitalize
  }

  def main(args: Array[String]) {
    val inputStr: Option[String] = args.length match {
      case 0 => None
      case _ => Some(args(0))
    }
    inputStr.map(Capitalize_String).map(println)
  }
}
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- manasmithamn

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).