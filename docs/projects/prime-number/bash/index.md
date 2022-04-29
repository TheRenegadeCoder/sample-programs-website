---

title: Prime Number in Bash
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Prime Number in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Bash
#!/bin/bash

ERROR="Usage: please input a non-negative integer"

# based on https://stackoverflow.com/questions/45392068/check-if-a-number-is-a-prime-in-bash
function is_prime(){
    if [[ $1 -eq 2 ]] || [[ $1 -eq 3 ]]; then
        return 1  # prime
    fi
    if [[ $(($1 % 2)) -eq 0 ]] || [[ $(($1 % 3)) -eq 0 ]] || [[ $1 -eq 1 ]]; then
        return 0  # not a prime
    fi
    i=5; w=2
    while [[ $((i * i)) -le $1 ]]; do
        if [[ $(($1 % i)) -eq 0 ]]; then
            return 0  # not a prime
        fi
        i=$((i + w))
        w=$((6 - w))
    done
    return 1  # prime
}

# validate input number
if [[ -z "${1}" ]]
then
	echo "${ERROR}"
	exit 1
fi

if ! [[ "${1}" =~ ^[0-9]+$ ]]
then
  echo "${ERROR}"
  exit 1
fi

# sample usage
is_prime ${1}
if [[ $? -eq 0 ]];
then
  echo "composite"
else
  echo "prime"
fi

exit 0

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.