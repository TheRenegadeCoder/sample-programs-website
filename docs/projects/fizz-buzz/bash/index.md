---

---

Welcome to the Fizz Buzz in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Bash
#!/bin/bash

for i in {1..100}; do
    if (( $i % 15 == 0 )); then
        echo "FizzBuzz"
    elif (( $i % 5 == 0 )); then
        echo "Buzz"
    elif (( $i % 3 == 0 )); then
        echo "Fizz"
    else
        echo $i
    fi
done

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.