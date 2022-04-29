---

title: Capitalize in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Capitalize in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Go
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.