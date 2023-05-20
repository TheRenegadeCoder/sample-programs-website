---
title: Selection Sort in Go
layout: default
date: 2019-03-18
featured-image: selection-sort-in-every-language.jpg
last-modified: 2019-03-18

---

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "encoding/json"
    "fmt"
    "math"
    "os"
    "regexp"
    "strconv"
    "strings"
)

func selectionSort(unsorted []int, sorted ...int) []int {
    if len(unsorted) <= 0 {
        return sorted
    }
    if len(unsorted) == 1 {
        return append(sorted, unsorted...)
    }

    min := math.MaxInt32
    minI := -1
    for i, n := range unsorted {
        if n < min {
            min = n
            minI = i
        }
    }
    sorted = append(sorted, min)
    unsorted = append(unsorted[:minI], unsorted[minI+1:]...)
    return selectionSort(unsorted, sorted...)
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

func sliceIntToString(list []int) (out string) {
    bytes, _ := json.Marshal(list)
    out = strings.Replace(string(bytes), ",", ", ", -1)
    out = strings.Trim(out, "[]")
    return
}

func exitWithError() {
    fmt.Println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    nums := strToSliceInt(os.Args[1])
    nums = selectionSort(nums)
    fmt.Println(sliceIntToString(nums))
}
```

{% endraw %}

[Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 25 2019 19:45:18. The solution was first committed on Mar 18 2019 00:51:47. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).