---
title: Binary Search in Go
layout: default
date: 2019-10-24
featured-image: binary-search-in-every-language.jpg
last-modified: 2019-10-24

---

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "encoding/json"
    "fmt"
    "os"
    "regexp"
    "strconv"
    "strings"
)

func binarySearch(list []int, target int) bool {
    midIndex := len(list) / 2
    midpoint := list[midIndex]

    if midpoint == target {
        return true
    }

    if len(list) <= 1 {
        return false
    }

    if target < list[midIndex] {
        return binarySearch(list[:midIndex], target)
    }

    return binarySearch(list[midIndex:], target)
}

func verifySortedList(list []int) {
    lastVal := list[0]
    for _, val := range list {
        if val < lastVal {
            exitWithError()
        }
    }
}

func strToSliceInt(strList string) []int {
    list := regexp.MustCompile(", ?").Split(strList, -1)
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
    fmt.Println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 3 {
        exitWithError()
    }

    list := strToSliceInt(os.Args[1])
    verifySortedList(list)
    target, err := strconv.Atoi(os.Args[2])
    if err != nil {
        exitWithError()
    }
    fmt.Println(binarySearch(list, target))
}
```

{% endraw %}

[Binary Search](https://sampleprograms.io/projects/binary-search) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).