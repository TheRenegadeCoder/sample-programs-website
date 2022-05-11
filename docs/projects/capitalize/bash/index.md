---

title: Capitalize in Bash
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Capitalize in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: please provide a string"
    exit 1
fi

echo ${1^}
```

{% endraw %}

Capitalize in Bash was written by:

- lohxx
- Jeremy Grifski

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 23:22:44. The solution was first committed on Oct 08 2019 21:12:31. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).