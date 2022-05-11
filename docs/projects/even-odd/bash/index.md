---

title: Even Odd in Bash
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Even Odd in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
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

Even Odd in Bash was written by:

- allievo-sudo
- Jeremy Grifski

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 29 2019 15:23:13. The solution was first committed on Oct 09 2019 16:02:54. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).