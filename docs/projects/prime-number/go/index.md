---

title: Prime Number in Go
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Prime Number in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	} else {
		for i := 2; i <= n/2; i++ {
			if n%i == 0 {
				return false
			}
		}
	}
	return true
}

func exitWithError() {
	fmt.Println("Usage: please input a non-negative integer")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil || n < 0 {
		exitWithError()
	}

	if isPrime(n) {
		fmt.Println("Prime")
	} else {
	    fmt.Println("Composite")
	}
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).