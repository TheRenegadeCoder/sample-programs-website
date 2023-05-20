---
title: Capitalize in Go
layout: default
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-09

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strings"
)

func exitWithError() {
    fmt.Println("Usage: please provide a string")
    os.Exit(1)
}

func uppercaseFirst(str string) string {
    s := string(str[0])
    u := strings.ToUpper(s)
    up := u + str[1:]
    return up
}

func main() {
    if len(os.Args) != 2 || len(os.Args[1]) == 0 {
        exitWithError()
    }

    s := os.Args[1]
    up := uppercaseFirst(s)

    fmt.Println(up)
}
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Go](https://sampleprograms.io/languages/go) was written by:

- Jeremy Grifski
- Nathaniel Niosco

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 20:30:14. The solution was first committed on Oct 09 2019 21:50:12. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).