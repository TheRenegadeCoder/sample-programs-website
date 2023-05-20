---
title: Longest Word in Go
layout: default
date: 2023-03-19
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-03-19

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strings"
)

const errorMessage = "Usage: please provide a string"

// longestWordLength returns the length of the longest word
// in a string. The words in the string should be separated
// by spaces, tabs, newlines, and/or carriage returns.
func longestWordLength(str string) int {
    words := strings.FieldsFunc(str, isLimitedWhitespace)
    return longestStringLength(words)
}

// isLimitedWhitespace returns whether a rune is one of four
// whitespace runes: ' ', '\t', '\n', '\r'
// Note that this is NOT equivalent to unicode.IsSpace which
// includes addtional whitespace runes
func isLimitedWhitespace(r rune) bool {
    return strings.ContainsRune(" \t\n\r", r)
}

// longestStringLength returns the length of the longest string
// in the slice
func longestStringLength(strs []string) (longest int) {
    for _, str := range strs {
        if len(str) > longest {
            longest = len(str)
        }
    }
    return
}

func main() {
    if len(os.Args) < 2 || len(os.Args[1]) == 0 {
        fmt.Println(errorMessage)
    } else {
        fmt.Println(longestWordLength(os.Args[1]))
    }
}
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Go](https://sampleprograms.io/languages/go) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).