---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: fraction-math-in-every-language.jpg
last-modified: 2025-10-09
layout: default
tags:
- fraction-math
- tcl
title: Fraction Math in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/tcl/how-to-implement-the-solution.md
- sources/programs/fraction-math/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
oo::class create Fraction {
	variable numer denom

	constructor {fractionStr} {
		if {[regexp {^\s*(-?\d+)\s*/\s*(\d+)\s*$} $fractionStr -> n d]} {
			# NUM/DEN format
		} elseif {[regexp {^\s*(-?\d+)$} $fractionStr -> n]} {
			# Integer format
			set n $n
			set d 1
		} else {
			error "Invalid fraction: $fractionStr"
		}

		set numer [expr {$n}]
		set denom [expr {$d}]

		if {$denom == 0} { error "Denominator cannot be zero" }

		set a [expr {abs($numer)}]
		set b [expr {abs($denom)}]
		while {$b != 0} {
			set t $b
			set b [expr {$a % $b}]
			set a $t
		}
		set g $a

		set numer [expr {($numer / $g) * ($denom < 0 ? -1 : 1)}]
		set denom [expr {abs($denom) / $g}]
	}

	method numer {} {return $numer}
	method denom {} {return $denom}

	method print {} { return ($denom == 1) ? "$numer" : "$numer/$denom" }

	method _binOp {other op} {
		set on [$other numer]
		set od [$other denom]
		switch -- $op {
			+ {set n [expr {$numer * $od + $on * $denom}]; set d [expr {$denom * $od}]}
			- {set n [expr {$numer * $od - $on * $denom}]; set d [expr {$denom * $od}]}
			* {set n [expr {$numer * $on}]; set d [expr {$denom * $od}]}
			/ {
				if {$on == 0} { error "Division by zero" }
				set n [expr {$numer * $od}]
				set d [expr {$denom * $on}]
			}
		}
		return [Fraction new "$n/$d"]
	}

	method add {other} {return [my _binOp $other +]}
	method sub {other} {return [my _binOp $other -]}
	method mult {other} {return [my _binOp $other *]}
	method div {other} {return [my _binOp $other /]}

	method _cross {other} {
		set on [$other numer]
		set od [$other denom]
		return [expr {$numer * $od - $on * $denom}]
	}

	method eq {other} {return [expr {[my _cross $other] == 0}]}
	method ne {other} {return [expr {[my _cross $other] != 0}]}
	method lt {other} {return [expr {[my _cross $other] < 0}]}
	method le {other} {return [expr {[my _cross $other] <= 0}]}
	method gt {other} {return [expr {[my _cross $other] > 0}]}
	method ge {other} {return [expr {[my _cross $other] >= 0}]}
}

if {[llength $argv] != 3} {
	puts "Usage: ./fraction-math operand1 operator operand2"
	exit 1
}

set op1  [string trim [lindex $argv 0]]
set oper [string trim [lindex $argv 1]]
set op2  [string trim [lindex $argv 2]]

if {[catch {set f1 [Fraction new $op1]} err]} {
    puts "Error: $err"
    exit 1
}
if {[catch {set f2 [Fraction new $op2]} err]} {
    puts "Error: $err"
    exit 1
}

set opMap [dict create \
    + add - sub * mult / div \
    == eq != ne > gt < lt >= ge <= le]

if {![dict exists $opMap $oper]} {
    puts "Unknown operator: $oper"
    exit 1
}

set result [$f1 [dict get $opMap $oper] $f2]

if {[lsearch -exact {+ - * /} $oper] != -1} {
    puts [$result print]
} else {
    puts $result
}


```

{% endraw %}

Fraction Math in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).