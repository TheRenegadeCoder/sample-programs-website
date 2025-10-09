---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- linear-search
- tcl
title: Linear Search in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/tcl/how-to-implement-the-solution.md
- sources/programs/linear-search/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")}
	exit 1
}

proc parseList {s} {
	set tokens [split [string trim $s] ","]
	if {[llength $tokens] < 1} { usage }

	set result {}

	set result {}
	foreach token $tokens {
		set t [string trim $token]
		if {$t eq "" || [catch {expr {int($t)}} val]} usage
		lappend result $val
	}
	return $result
}


proc parseInt {s} {
	set s [string trim $s]
	if {$s eq "" || [catch {expr {int($s)}} val]} {
		usage
	}
	return $val
}

proc linearSearch {nums value} {
	expr {[lsearch -integer -exact $nums $value] != -1}
}

if {$argc != 2} { usage }

set numbers [parseList [lindex $argv 0]]
set key     [parseInt  [lindex $argv 1]]

set found [linearSearch $numbers $key]
puts [expr {$found ? "true" : "false"}]


```

{% endraw %}

Linear Search in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).