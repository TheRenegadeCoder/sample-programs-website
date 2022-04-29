---

title: Baklava in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.