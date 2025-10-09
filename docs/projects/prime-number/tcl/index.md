---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- prime-number
- tcl
title: Prime Number in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/tcl/how-to-implement-the-solution.md
- sources/programs/prime-number/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require math::numtheory

proc usage {} {
    puts stderr {Usage: please input a non-negative integer}
    exit 1
}

proc isNonNegativeInteger {s} {
    if {[catch {expr {int($s)}} n]} {
        return 0
    }
    if {$s eq ""} { return 0 }
    if {![string is integer -strict $s]} {
        return 0
    }
    return [expr {$n >= 0}]
}

if {$argc != 1} { usage }

set input [string trim [lindex $argv 0]]
if {![isNonNegativeInteger $input]} { usage }

set n $input
if {$n < 2} {
    puts "composite"
} elseif {[math::numtheory::isprime $n]} {
    puts "prime"
} else {
    puts "composite"
}


```

{% endraw %}

Prime Number in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).