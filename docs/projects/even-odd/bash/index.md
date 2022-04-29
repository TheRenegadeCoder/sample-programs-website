---

title: Even Odd in Bash
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Even Odd in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Bash
#!/bin/bash
count=$1

[[ $count =~ ^[-+]?[0-9]+$ ]] || { echo "Usage: please input a number"; exit 1; }

rem=$(( $count % 2 ))
 
if [ $rem -eq 0 ]
then
    echo "Even"
else
    echo "Odd"
fi

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.