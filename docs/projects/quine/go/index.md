---

title: Quine in Go
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Quine in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import "fmt"

func main() {
	a := "package main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := %q\n\tfmt.Printf(a, a)\n}\n"
	fmt.Printf(a, a)
}
```

{% endraw %}

Quine in Go was written by:

- Parker Johansen

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).