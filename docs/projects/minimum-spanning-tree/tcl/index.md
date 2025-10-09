---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- minimum-spanning-tree
- tcl
title: Minimum Spanning Tree in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/tcl/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require struct::graph
package require struct::graph::op

proc usage {} {
	puts stderr {Usage: please provide a comma-separated list of integers}
	exit 1
}

proc isInteger {x} { return [string is integer -strict $x] }

proc parseList {s} {
	set s [string trim $s]
	if {$s eq ""} { usage }

	set result {}
	foreach t [split $s ,] {
		set t [string trim $t]
		if {![isInteger $t] || $t < 0} { usage }
		lappend result $t
	}
	return $result
}

proc range {start end} {
	set result {}
	for {set i $start} {$i <= $end} {incr i} { lappend result $i }
	return $result
}

proc createGraph {matrix} {
	set n [expr {int(sqrt([llength $matrix]))}]
	if {$n * $n != [llength $matrix]} { usage }

	set g [::struct::graph]
	$g node insert {*}[range 0 [expr {$n-1}]]

	set idx 0
	for {set i 0} {$i < $n} {incr i} {
		for {set j 0} {$j < $n} {incr j} {
			set w [lindex $matrix $idx]
			incr idx
			if {$w > 0} { 
				$g arc setweight [$g arc insert $i $j] $w 
			}
		}
	}
	return $g
}

if {[llength $argv] != 1} { usage }
set matrixStr [lindex $argv 0]

set matrix [parseList $matrixStr]
set g [createGraph $matrix]

try {
	set mst [::struct::graph::op::prim $g]
	set arcWeights [$g arc weights]

	set totalWeight 0
	foreach a $mst {
		incr totalWeight [dict get $arcWeights $a]
	}

	puts $totalWeight
} on error {err opts} {
	usage
} finally {
	$g destroy
}


```

{% endraw %}

Minimum Spanning Tree in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).