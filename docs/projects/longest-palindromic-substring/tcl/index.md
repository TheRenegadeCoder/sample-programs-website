---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- longest-palindromic-substring
- tcl
title: Longest Palindromic Substring in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/tcl/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
    puts stderr {Usage: please provide a string that contains at least one palindrome}
    exit 1
}

proc longestPalindromicSubstring {s} {
    if {$s eq ""} { return "" }

    set processed "#[join [split $s ""] #]#"
    set n [string length $processed]
    set p [lrepeat $n 0]

    set center 0
    set right 0
    set maxLen 0
    set maxCenter 0

    for {set i 0} {$i < $n} {incr i} {
        set mirror [expr {2 * $center - $i}]
        if {$i < $right} {
            lset p $i [expr {min($right - $i, [lindex $p $mirror])}]
        }

        while {
            ($i + [lindex $p $i] + 1) < $n &&
            ($i - [lindex $p $i] - 1) >= 0 &&
            [string index $processed [expr {$i + [lindex $p $i] + 1}]] eq \
            [string index $processed [expr {$i - [lindex $p $i] - 1}]]
        } {
            lset p $i [expr {[lindex $p $i] + 1}]
        }

        if {$i + [lindex $p $i] > $right} {
            set center $i
            set right [expr {$i + [lindex $p $i]}]
        }

        if {[lindex $p $i] > $maxLen} {
            set maxLen [lindex $p $i]
            set maxCenter $i
        }
    }

    set start [expr {($maxCenter - $maxLen) / 2}]

    return [string range $s $start [expr {$start + $maxLen - 1}]]
}

if {$argc != 1} { usage }

set input [string trim [lindex $argv 0]]
if {$input eq ""} { usage }

set result [longestPalindromicSubstring $input]
if {[string length $result] <= 1} { usage } 

puts $result


```

{% endraw %}

Longest Palindromic Substring in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).