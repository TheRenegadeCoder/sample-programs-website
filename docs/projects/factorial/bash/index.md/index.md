---

---

# Factorial in Bash

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Bash
#!/bin/bash

number=$1

if [[ -z "$number" ]]
then
	echo "Usage: please input a non-negative integer"
	exit 1
fi

if ! [[ "$number" =~ ^[0-9]+$ ]]  
then 
        echo "Usage: please input a non-negative integer"
        exit 1
fi

value=1

while [ $number -gt 1 ]
do

  value=$((value * number))
 
  number=$((number - 1))

done

echo $value

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.