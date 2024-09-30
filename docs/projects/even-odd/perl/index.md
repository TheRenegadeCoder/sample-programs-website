---
authors:
- "Gabriela Kandov\xE1"
date: 2019-10-16
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- even-odd
- perl
title: Even Odd in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/perl/how-to-implement-the-solution.md
- sources/programs/even-odd/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

# accept input as argument
my ($number) = @ARGV;

if (!defined $number || $number !~ /^\-?\d+$/) {
	print "Usage: please input a number\n";
	exit;
}

if ($number % 2 == 0) {
	print "Even\n";
} else {
	print "Odd\n";
}

```

{% endraw %}

Even Odd in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Gabriela Kandová

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).