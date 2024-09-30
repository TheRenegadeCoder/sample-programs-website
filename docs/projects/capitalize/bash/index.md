---
authors:
- Jeremy Grifski
- lohxx
date: 2019-10-08
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- bash
- capitalize
title: Capitalize in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/bash/how-to-implement-the-solution.md
- sources/programs/capitalize/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Capitalize in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jeremy Grifski
- lohxx

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).