---

---

# Baklava in Bash

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Bash
#!/bin/bash

for i in {0..9}; do
	printf " %.0s" $(seq 1 $(( 10 - $i )))
	printf "*%.0s" $(seq 1 $(( $i * 2 + 1 )))
	echo
done

printf "*%.0s" {1..21}
echo

for i in {9..0}; do
	printf " %.0s" $(seq 1 $(( 10 - $i )))
	printf "*%.0s" $(seq 1 $(( $i * 2 + 1 )))
	echo
done

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.