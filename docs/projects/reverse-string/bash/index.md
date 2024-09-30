---
authors:
- Abdus
- Parker Johansen
date: 2018-05-09
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-03-21
layout: default
tags:
- bash
- reverse-string
title: Reverse String in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/bash/how-to-implement-the-solution.md
- sources/programs/reverse-string/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Reverse String in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Abdus
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).