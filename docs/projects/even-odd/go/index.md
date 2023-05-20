---
title: Even Odd in Go
layout: default
date: 2018-10-25
featured-image: even-odd-in-every-language.jpg
last-modified: 2018-10-25

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func exitWithError() {
    fmt.Println("Usage: please input a number")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    n, err := strconv.Atoi(os.Args[1])
    if err != nil {
        exitWithError()
    }

    if n%2 == 0 {
        fmt.Printf("Even\n")
    } else {
        fmt.Printf("Odd\n")
    }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Go](https://sampleprograms.io/languages/go) was written by:

- clarkimusmax
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 01 2019 02:39:12. The solution was first committed on Oct 25 2018 20:22:28. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).