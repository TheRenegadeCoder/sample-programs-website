---

title: Reverse String in Scala
layout: default
date: 2022-04-28
last-modified: 2022-06-26

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.io.StdIn.readLine

object ReverseStringSample {
  // revese using recursive & pattern matching
  def reverseString(str: String): String = str.length match {
    case 0 => ""
    case 1 => str
    case _ => reverseString(tail(str)) ++ head(str)
  }

  def head(str: String): String = str.length match {
    case 0 => ""
    case _ => str.slice(0, 1)
  }

  def tail(str: String): String = str.length match {
    case 0 => ""
    case 1 => ""
    case _ => str.slice(1, str.length)
  }

  def main(args: Array[String]) {
    val inputStr: Option[String] = args.length match {
      case 0 => None
      case _ => Some(args(0))
    }
    inputStr.map(reverseString).map(println)
  }
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Vee Ng
- Viet Thang Nguyen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 22 2019 16:16:44. The solution was first committed on Mar 22 2019 12:59:04. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).