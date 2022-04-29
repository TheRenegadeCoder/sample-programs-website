---

title: Reverse String in Nim
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Reverse String in Nim page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Nim
# For reversing a string passed in as a parameter
import os
import strutils

var text: string
try:
    text = paramStr(1)
except IndexError:
    echo "Usage: please input a string to reverse"
    quit(1)

var reversed_text: string
for i in countdown(len(text)-1, 0):
  reversed_text = reversed_text & text[i]

echo reversed_text


```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.