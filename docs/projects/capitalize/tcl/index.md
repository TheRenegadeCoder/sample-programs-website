---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-07
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-10-07
layout: default
tags:
- capitalize
- tcl
title: Capitalize in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/tcl/how-to-implement-the-solution.md
- sources/programs/capitalize/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: please provide a string}
	exit 1
}

if {$argc < 1} { usage }

set buf [string trim [lindex $argv 0]]
if {$buf eq ""} { usage }

set first [string toupper [string index $buf 0]]
set rest [string range $buf 1 end]
puts "${first}${rest}"

```

{% endraw %}

Capitalize in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).