---

---

# Quine in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import "fmt"

func main() {
	a := "package main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := %q\n\tfmt.Printf(a, a)\n}\n"
	fmt.Printf(a, a)
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.