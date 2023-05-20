---
title: Reverse String in Bash
layout: default
date: 2018-05-09
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-05-09

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

string=$1
strLength=${#string}

for ((i=$strLength-1;i>-1;i--)); 
do
    reverseStr+=${string:i:1}
done
echo $reverseStr
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Abdus
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 21 2019 17:52:55. The solution was first committed on May 09 2018 11:32:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).