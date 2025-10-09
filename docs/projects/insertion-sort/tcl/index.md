---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- insertion-sort
- tcl
title: Insertion Sort in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/tcl/how-to-implement-the-solution.md
- sources/programs/insertion-sort/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

	set result {}
	foreach token $tokens {
		set t [string trim $token]
		if {$t eq "" || [catch {expr {int($t)}} val]} usage
		lappend result $val
	}
	return $result
}

proc isSorted {lst} {
	set prev [lindex $lst 0]
	foreach x [lrange $lst 1 end] {
		if {$x < $prev} {return 0}
		set prev $x
	}
	return 1
}

proc insertionSort {lstVar} {
    upvar 1 $lstVar lst
    set n [llength $lst]
    if {$n <= 1} {return}

    set findInsertPos [list {lst key high} {
        set low 0
        incr high -1
        while {$low <= $high} {
            set mid [expr {($low + $high) / 2}]
            if {[lindex $lst $mid] < $key} {
                incr low
            } else {
		incr high -1
	    }
        }
        return $low
    }]

    for {set i 1} {$i < $n} {incr i} {
        set key [lindex $lst $i]

        if {$key >= [lindex $lst [expr {$i - 1}]]} {
            continue
        }

        set pos [apply $findInsertPos $lst $key $i]

        set before [lrange $lst 0 [expr {$pos - 1}]]
        set middle [list $key]
        set after [lrange $lst $pos [expr {$i - 1}]]
        set rest [lrange $lst [expr {$i + 1}] end]

        set lst [concat $before $middle $after $rest]
    }
}

proc formatList {lst} { return [join $lst ", "] }

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]

if {![isSorted $numbers]} {
    insertionSort numbers
}

puts [formatList $numbers]

```

{% endraw %}

Insertion Sort in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).