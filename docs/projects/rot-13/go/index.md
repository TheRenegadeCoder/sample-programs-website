---

title: Rot 13 in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Rot 13 in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```go
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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).