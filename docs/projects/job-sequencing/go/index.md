---
title: Job Sequencing in Go
layout: default
date: 2019-03-16
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2019-03-16

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "math"
    "os"
    "regexp"
    "strconv"
)

type job struct {
    profit   int
    deadline int
}

type jobSequence []job
type jobMapping map[int]job

func maxProfit(jobs jobSequence) int {
    total := 0
    seq := iterateJobSequence(jobs, jobMapping{})
    for _, j := range seq {
        total += j.profit
    }
    return total
}

func iterateJobSequence(available jobSequence, complete jobMapping) jobMapping {
    if len(available) <= 0 {
        return complete
    }
    maxJob, available := available.popMax()
    if i := complete.newIndex(maxJob); i >= 0 {
        complete[i] = maxJob
    }
    return iterateJobSequence(available, complete)
}

func (mapping jobMapping) newIndex(maxJob job) int {
    var indexes []int
    for i := 0; i < maxJob.deadline; i++ {
        if _, ok := mapping[i]; !ok {
            indexes = append(indexes, i)
        }
    }
    if len(indexes) <= 0 {
        return -1
    }
    return indexes[len(indexes)-1]
}

func (seq jobSequence) popMax() (job, jobSequence) {
    max := job{math.MinInt32, math.MinInt32}
    maxI := -1
    for i, v := range seq {
        if v.profit > max.profit {
            max = v
            maxI = i
        }
    }
    return max, append(seq[:maxI], seq[maxI+1:]...)
}

func buildJobSequence(profits []int, deadlines []int) (jobs jobSequence) {
    for i, profit := range profits {
        newJob := job{profit: profit, deadline: deadlines[i]}
        jobs = append(jobs, newJob)
    }
    return
}

func exitWithError() {
    fmt.Println("Usage: please provide a list of profits and a list of deadlines")
    os.Exit(1)
}

func strToSliceInt(strList string) []int {
    list := regexp.MustCompile(", ?").Split(strList, -1)
    if len(list) < 2 {
        exitWithError()
    }
    var nums []int
    for _, num := range list {
        n, err := strconv.Atoi(num)
        if err != nil {
            exitWithError()
        }
        nums = append(nums, n)
    }
    return nums
}

func main() {
    if len(os.Args) != 3 {
        exitWithError()
    }

    profits := strToSliceInt(os.Args[1])
    deadlines := strToSliceInt(os.Args[2])
    if len(profits) != len(deadlines) {
        exitWithError()
    }
    jobs := buildJobSequence(profits, deadlines)
    max := maxProfit(jobs)
    fmt.Println(max)

}
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 25 2019 11:27:20. The solution was first committed on Mar 16 2019 16:00:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).