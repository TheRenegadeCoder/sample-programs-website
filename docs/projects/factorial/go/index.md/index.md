---

---

# Factorial in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func factorial(n uint64) uint64 {
	if n <= 0 {
		return 1
	}
	return n * factorial(n-1)
}

func exitWithError(msg string) {
	fmt.Println(msg)
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError("Usage: please input a non-negative integer")
	}
	n, err := strconv.ParseUint(os.Args[1], 0, 64)
	if err != nil {
		exitWithError("Usage: please input a non-negative integer")
	}
	if n > 65 {
		exitWithError(fmt.Sprintf("!%d is out of the reasonable bounds for calculation", n))
	}
	fmt.Println(factorial(n))
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.