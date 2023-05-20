---
title: Job Sequencing in Kotlin
layout: default
date: 2020-10-08
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2020-10-08

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) {
    val jobs = buildJobs(args)
    if (jobs.isNullOrEmpty()) {
        println("Usage: please provide a list of profits and a list of deadlines")
    } else {
        println(maxProfit(jobs))
    }
}

/**
 * Calculates the maximum profit of a list of jobs
 */
private fun maxProfit(jobs: List<Job>): Int {
    val scheduled = hashSetOf<Int>()
    var profit = 0
    jobs.sortedByDescending { it.profit }.forEach {
        for (i in it.deadline downTo 1) {
            if (scheduled.add(i)) {
                profit += it.profit
                break
            }
        }
    }
    return profit
}

/**
 * Builds job list with input arguments
 */
private fun buildJobs(args: Array<String>): List<Job>? {
    if (args.run { isNullOrEmpty() || size < 2 || any { it.isBlank() } }) return null

    val profits = args[0].toIntArray()
    val deadlines = args[1].toIntArray()

    if (profits.size != deadlines.size) return null
    return profits.mapIndexed { index, profit -> Job(profit, deadlines[index]) }
}

/**
 * Represents the information of a job
 */
class Job(val profit: Int, val deadline: Int)

/**
 * Extracts an array of integers from the string
 */
fun String.toIntArray() = split(",").mapNotNull { it.trim().toIntOrNull() }
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:34:00. The solution was first committed on Oct 08 2020 21:50:57. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).