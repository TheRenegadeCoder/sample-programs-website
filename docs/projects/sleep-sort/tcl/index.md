---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- sleep-sort
- tcl
title: Sleep Sort in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/tcl/how-to-implement-the-solution.md
- sources/programs/sleep-sort/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6

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

proc sleepSort {lst} {
    set ::sortedList {}
    set ::done 0

    foreach num $lst {
        after [expr {$num * 10}] [list lappend ::sortedList $num]
    }

    set max [lindex $lst 0]
    foreach n $lst {if {$n > $max} {set max $n}}

    after [expr {$max * 10 + 50}] {set ::done 1}
    vwait ::done

    return $::sortedList
}

proc formatList {lst} { return [join $lst ", "] }

if {$argc != 1} { usage }

set numbers [parseList [lindex $argv 0]]
set result [sleepSort $numbers]
puts [formatList $result]


```

{% endraw %}

Sleep Sort in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).