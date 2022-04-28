---

---

# Rot 13 in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"fmt"
	"os"
	"strings"
)

func rot13(str string) string {
	return strings.Map(encryptRune, str)
}

func encryptRune(r rune) rune {
	if r >= 65 && r <= 90 {
		return (((r - 65) + 13) % 26) + 65
	} else if r >= 97 && r <= 122 {
		return (((r - 97) + 13) % 26) + 97
	} else {
		return r
	}
}

func exitWithError() {
	fmt.Println("Usage: please provide a string to encrypt")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	if len(os.Args[1]) <= 0 {
	    exitWithError()
	}

	fmt.Println(rot13(os.Args[1]))
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.