---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- depth-first-search
- tcl
title: Depth First Search in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/tcl/how-to-implement-the-solution.md
- sources/programs/depth-first-search/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require struct ;# for struct::graph

proc usage {} {
	puts stderr {Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")}
	exit 1
}

proc isInteger {x} { return [string is integer -strict $x] }

proc parseList {s} {
	set s [string trim $s]
	if {$s eq ""} { usage }

	lmap t [split $s ","] {
		set t [string trim $t]
		if {![isInteger $t]} { usage }
		set t
	}
}

proc createGraph {matrix vertices} {
	set n [llength $vertices]
	if {[llength $matrix] != [expr {$n * $n}]} { usage }

	set g [struct::graph]
	foreach v $vertices { $g node insert $v }

	for {set i 0} {$i < $n} {incr i} {
		for {set j 0} {$j < $n} {incr j} {
			if {[lindex $matrix [expr {$i*$n + $j}]] != 0} {
				set a [lindex $vertices $i]
				set b [lindex $vertices $j]
				$g arc insert $a $b
			}
		}
	}
	return $g
}

proc dfsCommand {target visitedRef foundRef args} {
	upvar $visitedRef visited
	upvar $foundRef found

	set event  [lindex $args 0]
	set graph  [lindex $args 1]
	set node   [lindex $args 2]

	# We're only interested in what happens once we enter a node, not when
	# we leave it.
	if {$event ne "enter"} { return }

	if {[lsearch -exact $visited $node] >= 0} { return }

	lappend visited $node
	if {$node eq $target} { set found 1 }
}

proc dfs {graph start target} {
	set found 0
	set visited {}

	# Tcllib has DFS directly in struct::graph. However, to use it for this
	# I need a callback to tell me whether the target was found. It is quite
	# flexible, in typical Tcl fashion, but I don't need it to do very much.	
	$graph walk $start -type dfs -dir forward \
		-command [list dfsCommand $target visited found]

	return $found
}

if {$argc != 3} { usage }

set adjMatrix [parseList [lindex $argv 0]]
set vertices  [parseList [lindex $argv 1]]
set target	  [lindex $argv 2]

if {![isInteger $target]} { usage }

set graph [createGraph $adjMatrix $vertices]
set root  [lindex $vertices 0]

puts [expr {[dfs $graph $root $target] ? "true" : "false"}]


```

{% endraw %}

Depth First Search in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).