# Capitalize in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.