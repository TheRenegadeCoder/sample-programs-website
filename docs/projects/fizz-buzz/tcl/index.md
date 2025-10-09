---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-10-09
layout: default
tags:
- fizz-buzz
- tcl
title: Fizz Buzz in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/tcl/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
# This approach is exclusively to show the capabilities and flexibility of Tcl.
# It doesn't deserve being this overengineered in the normal case. :P

proc fizzbuzz {rules {limit 100}} {
	namespace eval ::fizzbuzz {
		namespace export *
		namespace ensemble create
	}

	foreach {div word} $rules {
		proc ::fizzbuzz::$word {n} [format {
			expr {($n %% %d) == 0 ? "%s" : ""}
		} $div $word]
	}

	for {set n 1} {$n <= $limit} {incr n} {
		set s ""
		foreach {div word} $rules {
			append s [::fizzbuzz::$word $n]
		}
		puts [expr {$s eq "" ? $n : $s}]
	}
}

fizzbuzz {3 Fizz 5 Buzz}

```

{% endraw %}

Fizz Buzz in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).