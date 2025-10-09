---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- tcl
- transpose-matrix
title: Transpose Matrix in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/tcl/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
package require Tcl 8.6
package require struct::matrix

proc usage {} {
	puts stderr {Usage: please enter the dimension of the matrix and the serialized matrix}
	exit 1
}

if {$argc != 3} { usage }
set cols [lindex $argv 0]
set rows [lindex $argv 1]
set matrixStr [lindex $argv 2]

if {$cols eq "" || $rows eq "" || $matrixStr eq ""} { usage }

if {![string is integer -strict $cols] || ![string is integer -strict $rows]} {
    usage
}

set values [lmap v [split $matrixStr ","] {string trim $v}]
if {[llength $values] != $cols * $rows} { usage }

set m [struct::matrix]
$m add columns $cols
$m add rows $rows

for {set r 0} {$r < $rows} {incr r} {
	set start [expr {$r*$cols}]
	set end [expr {($r+1)*$cols - 1}]
	$m set row $r [lrange $values $start $end]
}

$m transpose

set outList {}
for {set i 0} {$i < $cols} {incr i} {
    lappend outList {*}[$m get row $i]
}

puts [join $outList ", "]


```

{% endraw %}

Transpose Matrix in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).