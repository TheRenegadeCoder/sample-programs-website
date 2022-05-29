---

title: Quick Sort in Scala
layout: default
date: 2022-04-28
last-modified: 2022-05-29

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import scala.io.StdIn.readLine
import scala.reflect.ClassTag

object QuickSortSample {
  def main(args: Array[String]) {
    // verify inputs are being provided
    parseInput(args) match {
      case None => println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
      case Some(inputArr) => {
        val output = quicksort(inputArr).mkString(", ")
        println(output)
      }
    }
  }

  def parseInput(args: Array[String]): Option[Array[Int]] = args.length match {
    case 0 => None
    case _ => try {
      Some(args(0).split(",").map(_.trim).map(_.toInt))
    } catch {
      case e: Throwable => None
    }
  }

  // quick sort increasing elements
  // note on signature:
  // ClassTag elements help construct Array quen using ++ (instead of falling back to ArraySeq)
  // Elements of array implement Ordered, so we can compare 2 instances of T using ==, <, >, etc.
  def quicksort[T <% Ordered[T]: ClassTag](arr: Array[T]): Array[T] = arr.length match {
    case 0 => arr
    case 1 => arr
    case _ => {
      val pivot: T = arr(0)
      val lhs = arr.filter(_ < pivot)
      val mid = arr.filter(_ == pivot)
      val rhs = arr.filter(_ > pivot)

      quicksort(lhs) ++ mid ++ quicksort(rhs)
    }
  }
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Vee Ng
- Viet Thang Nguyen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 25 2019 19:52:01. The solution was first committed on Mar 22 2019 12:57:43. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).