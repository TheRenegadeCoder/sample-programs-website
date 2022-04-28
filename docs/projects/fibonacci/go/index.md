---

---

Welcome to the Fibonacci in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func fibonacci(n int, c chan int) {
	x, y := 1, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func exitWithError() {
	fmt.Println("Usage: please input the count of fibonacci numbers to output")
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

	c := make(chan int, n)

	go fibonacci(cap(c), c)
	i := 1
	for v := range c {
		fmt.Printf("%d: %d\n", i, v)
		i++
	}
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.