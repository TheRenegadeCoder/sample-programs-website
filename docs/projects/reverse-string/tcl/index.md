---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- reverse-string
- tcl
title: Reverse String in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/tcl/how-to-implement-the-solution.md
- sources/programs/reverse-string/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6

if {$argc != 1} { exit }

set input [lindex $argv 0]
if {$input eq ""} { exit }

puts [join [lreverse [split $input ""]] ""]


```

{% endraw %}

Reverse String in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).