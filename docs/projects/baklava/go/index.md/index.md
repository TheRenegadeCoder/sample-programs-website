---

---

# Baklava in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"fmt"
	"strings"
)

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}

	for i := 10; -1 < i; i-- {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.