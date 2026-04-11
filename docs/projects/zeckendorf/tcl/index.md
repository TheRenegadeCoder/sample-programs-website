---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-11
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-11
layout: default
tags:
- tcl
- zeckendorf
title: Zeckendorf in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/tcl/how-to-implement-the-solution.md
- sources/programs/zeckendorf/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts "Usage: please input a non-negative integer"
    exit 1
}

proc zeckendorf {n} {
    set result {}
    set a 1
    set b 2

    while {$b <= $n} {
        lassign [list $b [expr {$a + $b}]] a b
    }

    while {$n > 0} {
        if {$a <= $n} {
            set n [expr {$n - $a}]
            lappend result $a
        }
        lassign [list [expr {$b - $a}] $a] a b
    }

    return $result
}

if {$argc != 1} { usage }
lassign $argv arg

if {![string is integer -strict $arg] || $arg < 0} {
    usage
}

puts [join [zeckendorf $arg] ", "]
```

{% endraw %}

Zeckendorf in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).