---
title: Capitalize in Bash
layout: default
date: 2019-10-08
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-08

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jeremy Grifski
- lohxx

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 23:22:44. The solution was first committed on Oct 08 2019 21:12:31. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).