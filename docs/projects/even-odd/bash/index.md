---
authors:
- allievo-sudo
- Jeremy Grifski
date: 2019-10-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-29
layout: default
tags:
- bash
- even-odd
title: Even Odd in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/bash/how-to-implement-the-solution.md
- sources/programs/even-odd/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Even Odd in [Bash](https://sampleprograms.io/languages/bash) was written by:

- allievo-sudo
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).