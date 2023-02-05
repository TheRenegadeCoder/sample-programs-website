---

title: Reverse String in Go
layout: default
date: 2022-04-28
last-modified: 2023-02-05

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import "fmt"
import "os"

//Function to reverse a string
func reverse_string(str string) string {
	chars := []rune(str)
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	return string(chars)
}

func main() {
	// Check the command line args length
	var argslen = len(os.Args)

	// If the length is 2, one command line arg exist
	if argslen == 2 {
		input := os.Args[1]
		fmt.Printf("%v\n", reverse_string(input))
	} else { //No or more than two command line args exist
		fmt.Println("Input one string as command line arg")
	}
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen
- Riddhi K

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 01 2019 02:39:12. The solution was first committed on Oct 15 2018 21:21:39. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).