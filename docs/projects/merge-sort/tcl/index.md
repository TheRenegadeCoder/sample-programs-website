---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: merge-sort-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- merge-sort
- tcl
title: Merge Sort in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/tcl/how-to-implement-the-solution.md
- sources/programs/merge-sort/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"}
	exit 1
}

proc parseList {s} {
	set tokens [split [string trim $s] ","]
	if {[llength $tokens] < 2} { usage }

	set result {}
	foreach token $tokens {
		set t [string trim $token]
		if {$t eq "" || [catch {expr {int($t)}} val]} usage
		lappend result $val
	}
	return $result
}

proc merge {lstVar tempVar left mid right} {
	upvar 1 $lstVar lst
	upvar 1 $tempVar temp

	set i $left
	set j [expr {$mid + 1}]
	set k $left

	while {$i <= $mid && $j <= $right} {
		if {[lindex $lst $i] <= [lindex $lst $j]} {
			lset temp $k [lindex $lst $i]
			incr i
		} else {
			lset temp $k [lindex $lst $j]
			incr j
		}
		incr k
	}

	while {$i <= $mid} {
		lset temp $k [lindex $lst $i]
		incr i
		incr k
	}

	while {$j <= $right} {
		lset temp $k [lindex $lst $j]
		incr j
		incr k
	}

	for {set idx $left} {$idx <= $right} {incr idx} {
		lset lst $idx [lindex $temp $idx]
	}
}

proc mergeSort {lstVar} {
	upvar 1 $lstVar lst
	set n [llength $lst]
	if {$n <= 1} { return }

	set temp {}
	set width 1
	while {$width < $n} {
		set i 0
		while {$i < $n} {
			set left $i
			set mid [expr {$i + $width - 1}]
			if {$mid >= $n} { break }

			set right [expr {$mid + $width}]
			if {$right >= $n} { set right [expr {$n - 1}] }

			merge lst temp $left $mid $right
			incr i [expr {2 * $width}]
		}
		set width [expr {$width * 2}]
	}
}

proc formatList {lst} { return [join $lst ", "] }

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]
mergeSort numbers
puts [formatList $numbers]


```

{% endraw %}

Merge Sort in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).