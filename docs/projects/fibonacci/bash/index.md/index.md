---

---

Welcome to the Fibonacci in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Bash
#!/bin/bash

count=$1

[[ $count =~ ^[0-9]+$ ]] || { echo "Usage: please input the count of fibonacci numbers to output"; exit 1; }

n=1
n_minus_1=1
[[ $count < 1 ]] && exit 0

echo "1: 1"
for i in $(seq 2 $count); do
    echo "$i: $n"
    tmp=$n
    n=$[$n+$n_minus_1]
    n_minus_1=$tmp
done

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.