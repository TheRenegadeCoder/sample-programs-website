---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- job-sequencing
- tcl
title: Job Sequencing in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/tcl/how-to-implement-the-solution.md
- sources/programs/job-sequencing/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require math

proc usage {} {
	puts stderr {Usage: please provide a list of profits and a list of deadlines}
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

proc compareJobs {a b} {
	lassign $a _ aProfit aDeadline
	lassign $b _ bProfit bDeadline

	expr {
		($aProfit > $bProfit) ? -1 :
		($aProfit < $bProfit) ? 1  :
		($aDeadline > $bDeadline) ? -1 :
		($aDeadline < $bDeadline) ? 1  : 0
	}

}

proc jobSequencing {profits deadlines} {
	if {[llength $profits] != [llength $deadlines]} { usage }

	set jobs {}
	for {set i 0} {$i < [llength $profits]} {incr i} {
		set jobId    [expr {$i + 1}]
		set profit   [lindex $profits $i]
		set deadline [lindex $deadlines $i]
		lappend jobs [list $jobId $profit $deadline]
	}

	set jobs [lsort -command compareJobs $jobs]
	set maxDeadline [math::max {*}$deadlines]
	set slots [lrepeat $maxDeadline 0]
	set totalProfit 0

	foreach job $jobs {
		lassign $job jobId profit deadline
		set slotIndex [expr {$deadline - 1}]
		while {$slotIndex >= 0 && [lindex $slots $slotIndex]} {
			incr slotIndex -1
		}
		if {$slotIndex >= 0} {
			lset slots $slotIndex 1
			incr totalProfit $profit
		}
	}
	return $totalProfit
}

if {$argc != 2} {
	usage
}

set profits   [parseList [lindex $argv 0]]
set deadlines [parseList [lindex $argv 1]]

puts [jobSequencing $profits $deadlines]


```

{% endraw %}

Job Sequencing in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).