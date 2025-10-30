---
authors:
- Darien Arthur-Gocken
date: 2025-10-30
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- prime-number
- red
title: Prime Number in Red
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/red/how-to-implement-the-solution.md
- sources/programs/prime-number/red/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Red](https://sampleprograms.io/languages/red) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```red
Red [Title: "Prime Number in Red"]

prime-number: func [number [integer!]] [
    either number <= 1 [
        print "Composite"
    ][
        found?: false
        limit: to integer! square-root number
        repeat i limit - 1 [
            if (number // (i + 1)) = 0 [
                print "Composite"
                found?: true
                break
            ]
        ]
        if not found? [print "Prime"]
    ]
]

main: func [arg [string!]] [

    arg: trim/with arg {'"}

    digit: charset "0123456789"
    if not parse arg [opt ["+" | "-"] some digit end] [
        print "Usage: please input a non-negative integer"
        exit
    ]

    either attempt [arg: to-integer arg][
    ][
        print "Usage: please input a non-negative integer"
        exit
    ]

    if negative? arg [
        print "Usage: please input a non-negative integer"
        exit
    ]

    prime-number arg
]

main system/script/args
```

{% endraw %}

Prime Number in [Red](https://sampleprograms.io/languages/red) was written by:

- Darien Arthur-Gocken

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).