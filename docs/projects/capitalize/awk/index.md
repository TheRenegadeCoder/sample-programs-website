---
authors:
- rzuckerm
date: 2025-04-06
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-04-06
layout: default
tags:
- awk
- capitalize
title: Capitalize in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/awk/how-to-implement-the-solution.md
- sources/programs/capitalize/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string"
    exit(1)
}

function capitalize(s) {
    return toupper(substr(s, 1, 1)) substr(s, 2)
}

BEGIN {
    if (ARGC < 2 || !ARGV[1]) {
        usage()
    }

    print capitalize(ARGV[1])
}

```

{% endraw %}

Capitalize in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).