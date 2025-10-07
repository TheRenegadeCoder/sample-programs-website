---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- even-odd
- tcl
title: Even Odd in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/tcl/how-to-implement-the-solution.md
- sources/programs/even-odd/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
    puts "Usage: please input a number"
    exit 1
}

if {$argc != 1} {
    usage
}

set arg [lindex $argv 0]

if {![string is integer -strict $arg]} {
    usage
}

set num [expr {$arg + 0}]
puts [expr {$num % 2 == 0 ? "Even" : "Odd"}] 

```

{% endraw %}

Even Odd in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).