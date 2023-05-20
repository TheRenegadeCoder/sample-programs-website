---
title: Prime Number in Go
layout: default
date: 2019-05-02
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-05-02

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func isPrime(n int) bool {
    if n < 2 {
        return false
    } else {
        for i := 2; i <= n/2; i++ {
            if n%i == 0 {
                return false
            }
        }
    }
    return true
}

func exitWithError() {
    fmt.Println("Usage: please input a non-negative integer")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    n, err := strconv.Atoi(os.Args[1])
    if err != nil || n < 0 {
        exitWithError()
    }

    if isPrime(n) {
        fmt.Println("Prime")
    } else {
        fmt.Println("Composite")
    }
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 02 2019 11:43:38. The solution was first committed on May 02 2019 11:26:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).