---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- longest-word
- tcl
title: Longest Word in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/tcl/how-to-implement-the-solution.md
- sources/programs/longest-word/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: please provide a string}
	exit 1
}

proc longestWordLength {s} {
	set s [string trim $s]
	if {$s eq ""} { usage }

	set maxLen 0
	set curLen 0
	set len [string length $s]

	for {set i 0} {$i < $len} {incr i} {
		set ch [string index $s $i]
		if {[string is space $ch]} {
			if {$curLen > $maxLen} { set maxLen $curLen }
			set curLen 0
		} else {
			incr curLen
		}
	}

	if {$curLen > $maxLen} { set maxLen $curLen }

	return $maxLen
}

if {$argc != 1} { usage }

set input [lindex $argv 0]
if {[string trim $input] eq ""} { usage }

puts [longestWordLength $input]

```

{% endraw %}

Longest Word in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).