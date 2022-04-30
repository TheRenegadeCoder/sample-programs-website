---

title: Even Odd in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).