---
authors:
- Jeremy Grifski
- thetbl
date: 2019-10-14
featured-image: prime-number-in-every-language.jpg
last-modified: 2021-05-22
layout: default
tags:
- bash
- prime-number
title: Prime Number in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/bash/how-to-implement-the-solution.md
- sources/programs/prime-number/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
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

Prime Number in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jeremy Grifski
- thetbl

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).