---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: rot13-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- rot13
- tcl
title: Rot13 in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/tcl/how-to-implement-the-solution.md
- sources/programs/rot13/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl

proc usage {} {
    puts "Usage: please provide a string to encrypt"
    exit 1
}

if {$argc != 1} { usage }
set input [lindex $argv 0]
if {$input eq ""} { usage }

proc rot13 {text} {
    set upper "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    set lower "abcdefghijklmnopqrstuvwxyz"

    set map {}

    for {set i 0} {$i < 26} {incr i} {
        lappend map [string index $upper $i] [string index $upper [expr {($i+13)%26}]]
        lappend map [string index $lower $i] [string index $lower [expr {($i+13)%26}]]
    }

    return [string map $map $text]
}

puts [rot13 $input]


```

{% endraw %}

Rot13 in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).