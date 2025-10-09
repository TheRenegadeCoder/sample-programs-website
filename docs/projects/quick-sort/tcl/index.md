---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: quick-sort-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- quick-sort
- tcl
title: Quick Sort in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/tcl/how-to-implement-the-solution.md
- sources/programs/quick-sort/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

proc swap {varName i j} {
	upvar 1 $varName lst
	if {$i == $j} return
	set tmp [lindex $lst $i]
	lset lst $i [lindex $lst $j]
	lset lst $j $tmp
}

proc medianOfThree {varName a b c} {
	upvar 1 $varName lst
	set va [lindex $lst $a]
	set vb [lindex $lst $b]
	set vc [lindex $lst $c]
	if {$va <= $vb} {
		if {$vb <= $vc} { 
			return $b 
		} elseif {$va <= $vc} { 
			return $c 
		} else { 
			return $a 
		}
	} else {
		if {$va <= $vc} { 
			return $a 
		} elseif {$vb <= $vc} { 
			return $c 
		} else { 
			return $b 
		}
	}
}

proc medianOfNine {varName left right} {
	upvar 1 $varName lst
	set n [expr {$right - $left}]
	if {$n < 8} {
		set mid [expr {$left + $n / 2}]
		return [medianOfThree lst $left $mid $right]
	}
	set step [expr {$n / 8}]
	set mid [expr {$left + $n / 2}]
	set m1 [medianOfThree lst $left [expr {$left+$step}] [expr {$left+2*$step}]]
	set m2 [medianOfThree lst [expr {$mid-$step}] $mid [expr {$mid+$step}]]
	set m3 [medianOfThree lst [expr {$right-2*$step}] [expr {$right-$step}] $right]
	return [medianOfThree lst $m1 $m2 $m3]
}

proc quicksortInPlace {varName left right} {
	upvar 1 $varName lst

	while {$left < $right} {
		# median-of-nine pivot
		set pivotIndex [medianOfNine lst $left $right]
		set pivotValue [lindex $lst $pivotIndex]
		swap lst $pivotIndex $right

		# three-way partition
		set i $left
		set j $right
		set k $left
		while {$k <= $j} {
			set val [lindex $lst $k]
			if {$val < $pivotValue} {
				swap lst $k $i
				incr i
				incr k
			} elseif {$val > $pivotValue} {
				swap lst $k $j
				incr j -1
			} else {
				incr k
			}
		}

		# recurse on smaller side first (tail recursion elimination)
		set leftEnd [expr {$i - 1}]
		set rightStart [expr {$j + 1}]
		if {[expr {$leftEnd - $left}] < [expr {$right - $rightStart}]} {
			if {$left < $leftEnd} {
				quicksortInPlace lst $left $leftEnd
			}
			set left $rightStart
		} else {
			if {$rightStart < $right} {
				quicksortInPlace lst $rightStart $right
			}
			set right $leftEnd
		}
	}
}

proc quicksort {lst} {
	set n [llength $lst]
	if {$n <= 1} { return $lst }
	quicksortInPlace lst 0 [expr {$n - 1}]
	return $lst
}

proc formatList {lst} { return [join $lst ", "] }

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]
puts [formatList [quicksort $numbers]]


```

{% endraw %}

Quick Sort in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).