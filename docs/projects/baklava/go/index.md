---
title: Baklava in Go
layout: default
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    for i := 0; i < 10; i++ {
        fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
    }

    for i := 10; -1 < i; i-- {
        fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
    }
}
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Go](https://sampleprograms.io/languages/go) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 01 2019 02:39:12. The solution was first committed on Sep 17 2018 16:48:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).