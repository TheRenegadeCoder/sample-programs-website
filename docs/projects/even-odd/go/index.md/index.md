# Even Odd in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func exitWithError() {
	fmt.Println("Usage: please input a number")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		exitWithError()
	}

	if n%2 == 0 {
		fmt.Printf("Even\n")
	} else {
		fmt.Printf("Odd\n")
	}
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.