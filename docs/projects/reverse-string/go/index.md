---

title: Reverse String in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Reverse String in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Go
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.