---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- palindromic-number
- tcl
title: Palindromic Number in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/tcl/how-to-implement-the-solution.md
- sources/programs/palindromic-number/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6

proc usage {} {
    puts stderr "Usage: please input a non-negative integer"
    exit 1
}

proc isNonNegativeInteger {s} { return [regexp {^[0-9]+$} $s] }


proc isPalindrome {s} {
    set n [string length $s]
    set i 0
    set j [expr {$n - 1}]
    while {$i < $j} {
        if {[string range $s $i $i] ne [string range $s $j $j]} {
            return 0
        }
        incr i
        incr j -1
    }
    return 1
}

if {$argc != 1} { usage }

set input [string trim [lindex $argv 0]]
if {![isNonNegativeInteger $input]} { usage }

puts [expr {[isPalindrome $input] ? "true" : "false"}]

```

{% endraw %}

Palindromic Number in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).