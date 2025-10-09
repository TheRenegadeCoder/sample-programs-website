---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- maximum-subarray
- tcl
title: Maximum Subarray in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/tcl/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
proc usage {} {
	puts stderr {Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"}
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

proc maximumSubarraySum {numbers} {
    if {[llength $numbers] == 0} { return 0 }

    set currentSum [lindex $numbers 0]
    set maxSum $currentSum

    for {set i 1} {$i < [llength $numbers]} {incr i} {
        set val [lindex $numbers $i]
        set currentSum [expr {max($val, $currentSum + $val)}]
        set maxSum [expr {max($maxSum, $currentSum)}]
    }

    return $maxSum
}

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]
puts [maximumSubarraySum $numbers]

```

{% endraw %}

Maximum Subarray in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).