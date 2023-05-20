---
title: Factorial in Go
layout: default
date: 2019-02-24
featured-image: factorial-in-every-language.jpg
last-modified: 2019-02-24

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func factorial(n uint64) uint64 {
    if n <= 0 {
        return 1
    }
    return n * factorial(n-1)
}

func exitWithError(msg string) {
    fmt.Println(msg)
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError("Usage: please input a non-negative integer")
    }
    n, err := strconv.ParseUint(os.Args[1], 0, 64)
    if err != nil {
        exitWithError("Usage: please input a non-negative integer")
    }
    if n > 65 {
        exitWithError(fmt.Sprintf("!%d is out of the reasonable bounds for calculation", n))
    }
    fmt.Println(factorial(n))
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).