---
authors:
- rzuckerm
date: 2025-04-06
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-04-06
layout: default
tags:
- awk
- duplicate-character-counter
title: Duplicate Character Counter in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/awk/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string"
    exit(1)
}

function duplicate_character_counter(s, counts, order) {
    for (i = 1; i <= length(s); i++) {
        c = substr(s, i, 1)
        if (!(c in counts)) {
            order[i] = c
        }

        counts[c]++
    }
}

function display_duplicate_character_counts(counts, order) {
    dupes = 0
    for (idx in order) {
        c = order[idx]
        if (counts[c] > 1) {
            print c ": " counts[c]
            dupes = 1
        }
    }

    if (!dupes) {
        print "No duplicate characters"
    }
}

BEGIN {
    if (ARGC < 2 || !ARGV[1]) {
        usage()
    }

    s = ARGV[1]
    duplicate_character_counter(s, counts, order)
    display_duplicate_character_counts(counts, order)
}

```

{% endraw %}

Duplicate Character Counter in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).