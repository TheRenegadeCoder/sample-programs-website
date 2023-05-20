---
title: Longest Palindromic Substring in Go
layout: default
date: 2020-10-26
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2020-10-26

---

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "fmt"
    "os"
    "strings"
)

const errorMessage = "Usage: please provide a string that contains at least one palindrome"

func reverse(s string) string {
    result := ""
    for _, v := range s {
        result = string(v) + result
    }
    return result
}

func longestPalSubstr(str string) string {
    result := ""

    if len(str) < 2 || str == "" {
        return errorMessage
    }

    for i := 1; i < len(str); i++ {
        for j := 0; j < len(str)-i; j++ {
            possiblePal := strings.ToLower(str[j : j+i+1])

            if possiblePal == reverse(possiblePal) && len(possiblePal) > len(result) {
                result = possiblePal
            }

        }
    }

    if len(result) == 0 {
        result = errorMessage
    }
    return result
}

func printSubStr(str string, low, high int) string {
    s := ""
    for i := low; i <= high; i++ {
        s = s + string(str[i])
    }

    return s
}

func main() {
    if len(os.Args) < 2 {
        fmt.Println(errorMessage)
    } else {
        fmt.Println(longestPalSubstr(os.Args[1]))
    }
}
```

{% endraw %}

[Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Go](https://sampleprograms.io/languages/go) was written by:

- izexi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).