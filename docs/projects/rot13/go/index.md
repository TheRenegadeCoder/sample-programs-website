---
title: Rot13 in Go
layout: default
date: 2019-03-17
featured-image: rot13-in-every-language.jpg
last-modified: 2019-03-17

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strings"
)

func rot13(str string) string {
    return strings.Map(encryptRune, str)
}

func encryptRune(r rune) rune {
    if r >= 65 && r <= 90 {
        return (((r - 65) + 13) % 26) + 65
    } else if r >= 97 && r <= 122 {
        return (((r - 97) + 13) % 26) + 97
    } else {
        return r
    }
}

func exitWithError() {
    fmt.Println("Usage: please provide a string to encrypt")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    if len(os.Args[1]) <= 0 {
        exitWithError()
    }

    fmt.Println(rot13(os.Args[1]))
}
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 06 2019 00:32:12. The solution was first committed on Mar 17 2019 19:16:07. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).