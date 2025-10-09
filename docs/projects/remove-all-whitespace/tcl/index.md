---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- remove-all-whitespace
- tcl
title: Remove All Whitespace in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/tcl/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6

proc usage {} {
    puts stderr {Usage: please provide a string}
    exit 1
}

proc removeWhitespace {str} {
    regsub -all {\s} $str {} result
    return $result
}

if {$argc != 1} { usage }
set input [lindex $argv 0]
if {$input eq ""} { usage }

puts [removeWhitespace $input]

```

{% endraw %}

Remove All Whitespace in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).