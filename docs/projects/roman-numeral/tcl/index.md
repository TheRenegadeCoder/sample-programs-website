---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- roman-numeral
- tcl
title: Roman Numeral in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/tcl/how-to-implement-the-solution.md
- sources/programs/roman-numeral/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require math::roman

proc usage {msg} {
    puts $msg
    exit 1
}

if {$argc != 1} { usage "Usage: please provide a string of roman numerals" }

set input [string trim [lindex $argv 0]]

if {$input eq ""} {
    puts 0
    exit 0
}

if {[catch {math::roman::tointeger $input} err]} {
    usage "Error: invalid string of roman numerals"
} else {
    puts [math::roman::tointeger $input]
}

```

{% endraw %}

Roman Numeral in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).