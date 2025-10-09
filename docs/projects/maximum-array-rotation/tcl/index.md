---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- maximum-array-rotation
- tcl
title: Maximum Array Rotation in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/tcl/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: please provide a list of integers (e.g. "8, 3, 1, 2")}
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

proc maximumRotationSum {numbers} {
	set n [llength $numbers]
	if {$n == 0} { usage }

	set totalSum 0
	set currentSum 0
	for {set i 0} {$i < $n} {incr i} {
		set val [lindex $numbers $i]
		incr totalSum $val
		incr currentSum [expr {$val * $i}]
	}

	set maxSum $currentSum

	for {set i 1} {$i < $n} {incr i} {
		set rotatedVal [lindex $numbers [expr {$n - $i}]]
		set currentSum [expr {$currentSum + $totalSum - $n * $rotatedVal}]
		if {$currentSum > $maxSum} { set maxSum $currentSum }
	}

	return $maxSum
}

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]
puts [maximumRotationSum $numbers]

```

{% endraw %}

Maximum Array Rotation in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).