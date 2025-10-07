---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- fibonacci
- tcl
title: Fibonacci in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/tcl/how-to-implement-the-solution.md
- sources/programs/fibonacci/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
    puts "Usage: please input the count of fibonacci numbers to output"
    exit 1
}

if {$argc != 1} { usage }

set count [lindex $argv 0]

if {![string is integer -strict $count] || $count < 0} { usage }

set a 1
set b 1

for {set i 1} {$i <= $count} {incr i} {
    puts "$i: $a"

    set next [expr {$a + $b}]
    set a $b
    set b $next
}

```

{% endraw %}

Fibonacci in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).