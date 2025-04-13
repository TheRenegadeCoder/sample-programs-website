---
authors:
- Dani-DEV28
date: 2025-04-06
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2025-04-06
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
import scala.collection.mutable.ListBuffer
import scala.concurrent._
import ExecutionContext.Implicits.global
import scala.concurrent.duration._

object SleepSort {
  def main(args: Array[String]): Unit = {
    var result = invalidChecker(args)
      
    if(!result){ // After going through checker, it will output result to procede with SleepSort or not
      // println(result)
      println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
    } else {
      val numbers = args.flatMap(_.split(",")).map(_.trim).filter(_.nonEmpty).map(_.toInt)
      println(sleepSort(numbers))
    }
  }
    

  // Checking for formating, empty array, and Non-numeric values
  def invalidChecker(args: Array[String]): Boolean = args match {
    case null | Array() => false  // "No Input"
    case arr if arr.forall(_.isEmpty) =>  false //"Empty Input"
    case arr if arr.forall(_.length == 1) && arr.length == 1 => false //"Invalid Input: Not A List"
    case arr if !arr.exists(_.contains(",")) => false //"Invalid Input: Wrong Format"
    case _ =>  true
  }

  // delaying time to add a value to list base on it weight
  def sleepSort(args: Array[Int]): String = {
    val delayTimer: Long = 100L
    val output = new ListBuffer[Int]()

    val futures = args.map { num =>
      Future {
        blocking {
          Thread.sleep(num * delayTimer) // Delay execution
        }
        output.synchronized {
          output += num
        }
      }
    }.toList // Convert Array to List to fix type mismatch

    Await.result(Future.sequence(futures), Duration.Inf) // Wait for all futures
    output.mkString(", ") // Format output correctly
  }
}

```

{% endraw %}

Sleep Sort in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Dani-DEV28

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).