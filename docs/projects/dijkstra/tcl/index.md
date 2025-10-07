---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: dijkstra-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- dijkstra
- tcl
title: Dijkstra in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/tcl/how-to-implement-the-solution.md
- sources/programs/dijkstra/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require struct
package require struct::graph
package require struct::graph::op

proc usage {} {
	puts stderr {Usage: please provide three inputs: a serialized matrix, a source node and a destination node}
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

proc createGraph {matrix vertices} {
	set n [llength $vertices]
	if {[llength $matrix] != [expr {$n * $n}]} { usage }

	set g [struct::graph]
	$g node insert {*}$vertices

	set idx 0
	foreach i $vertices {
		foreach j $vertices {
			set w [lindex $matrix $idx]
			incr idx
			if {$w > 0} {
				set a [$g arc insert $i $j]
				$g arc setweight $a $w
			}
		}

		return $g
	}
}

proc main {argv} {
	if {[llength $argv] != 3} { usage }
	lassign $argv matrixStr srcStr destStr

	if {![string is integer -strict $srcStr] || ![string is integer -strict $destStr]} {
		usage
	}

	set matrix [parseList $matrixStr]
	set n [expr {int(sqrt([llength $matrix]))}]
	if {$n*$n != [llength $matrix]} { usage }

	set src  [expr {$srcStr + 0}]
	set dest [expr {$destStr + 0}]
	if {$src < 0 || $src >= $n || $dest < 0 || $dest >= $n} { usage }

	set vertices [lrange [list {*}[lrepeat $n 0]] 0 end]
	for {set i 0} {$i < $n} {incr i} { lset vertices $i $i }

	set g [createGraph $matrix $vertices]

	if {[$g node degree $src] == 0 || [$g node degree $dest] == 0} {
		$g destroy
		usage
	}

	try {
		set distances [::struct::graph::op::dijkstra $g $src -outputformat distances]
		if {[dict exists $distances $dest]} {
			puts [dict get $distances $dest]
		} else {
			usage
		}
	} on error {err opts} {
		usage
	} finally {
		$g destroy
	}
}

main $argv


```

{% endraw %}

Dijkstra in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).