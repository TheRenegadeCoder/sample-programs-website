---

title: Even Odd in Bash
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jeremy Grifski
- allievo-sudo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 29 2019 15:23:13. The solution was first committed on Oct 09 2019 16:02:54. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).