---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-11
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- scala
- sleep-sort
title: Sleep Sort in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/scala/how-to-implement-the-solution.md
- sources/programs/sleep-sort/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import java.util.concurrent.{CountDownLatch, Executors}
import java.util.{ArrayList, Collections}
import scala.util.Try
import scala.jdk.CollectionConverters._

object SleepSort {
  def main(args: Array[String]): Unit =
    args.toList match {
      case raw :: Nil =>
        val numbers = parse(raw)

        if (numbers.length < 2)
          usage()

        println(format(sleepSort(numbers)))

      case _ =>
        usage()
    }

  private def usage(): Nothing = {
    println("""Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"""")
    sys.exit(1)
  }

  private def parse(input: String): List[Int] =
    input
      .split(",")
      .iterator
      .map(_.trim)
      .filter(_.nonEmpty)
      .flatMap(s => Try(s.toInt).toOption)
      .toList
    match {
      case Nil => usage()
      case xs => xs
    }

  private def format(xs: List[Int]): String =
    xs.mkString(", ")

  private def sleepSort(input: List[Int]): List[Int] = {
    val sortedList = Collections.synchronizedList(new ArrayList[Int]())
    val executor = Executors.newCachedThreadPool()
    val latch = new CountDownLatch(input.size)

    input.foreach { n =>
      executor.submit(new Runnable {
        override def run(): Unit = {
          try {
            Thread.sleep(n.toLong * 100L)
            sortedList.add(n)
          } catch {
            case _: InterruptedException =>
              Thread.currentThread().interrupt()
          } finally {
            latch.countDown()
          }
        }
      })
    }

    latch.await()
    executor.shutdown()

    sortedList.asScala.toList
  }
}
```

{% endraw %}

Sleep Sort in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).