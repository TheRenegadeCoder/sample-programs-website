---

title: Baklava in Bash
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.