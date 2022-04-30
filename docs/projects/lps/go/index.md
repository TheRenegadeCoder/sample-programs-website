---

title: LPS in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the LPS in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Go
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).