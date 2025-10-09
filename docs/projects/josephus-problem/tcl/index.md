---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- josephus-problem
- tcl
title: Josephus Problem in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/tcl/how-to-implement-the-solution.md
- sources/programs/josephus-problem/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
    puts stderr {Usage: please input the total number of people and number of people to skip.}
    exit 1
}

proc parseInt {s} {
    set s [string trim $s]
    if {[string is integer -strict $s]} { return $s }
    usage
}

proc josephus {total skip} {
    if {$skip < 1 || $total < 1} { usage }

    # If skip = 1, survivor is the last person
    if {$skip == 1} { return $total }

    # Optimized case for skip = 2
    if {$skip == 2} {
        set power 1
        while {($power << 1) <= $total} {
            set power [expr {$power << 1}]
        }
        return [expr {2 * ($total - $power) + 1}]
    }

    set result 0
    for {set i 2} {$i <= $total} {incr i} {
        set result [expr {($result + $skip) % $i}]
    }

    return [expr {$result + 1}]
}

if {$argc != 2} { usage }

set total [parseInt [lindex $argv 0]]
set skip  [parseInt [lindex $argv 1]]

puts [josephus $total $skip]

```

{% endraw %}

Josephus Problem in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).