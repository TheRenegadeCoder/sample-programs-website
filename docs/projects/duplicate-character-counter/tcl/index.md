---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- duplicate-character-counter
- tcl
title: Duplicate Character Counter in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/tcl/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr "Usage: please provide a string"
	exit 1
}

proc countDuplicates {str} {
	set counts [dict create]
	set order {}

	foreach ch [split $str {}] {
		if {[string is alnum -strict $ch]} {
			if {![dict exists $counts $ch]} {
				lappend order $ch
			}
			dict incr counts $ch 1
		}
	}

	set printed 0

	foreach ch $order {
		set count [dict get $counts $ch]
		if {$count > 1} {
			puts "$ch: $count"
			incr printed
		}
	}

	if {$printed == 0} {
		puts "No duplicate characters"
	}
}

if {$argc != 1} { usage }

set input [string trim [lindex $argv 0]]
if {$input eq ""} { usage }

countDuplicates $input


```

{% endraw %}

Duplicate Character Counter in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).