---
authors:
- Bharath
- "Gabriela Kandov\xE1"
date: 2019-10-14
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- factorial
- perl
title: Factorial in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/perl/how-to-implement-the-solution.md
- sources/programs/factorial/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

# no input
usage() unless @ARGV == 1;

# accept input as argument
my ($number) = @ARGV;

# if not provided, read from standard input
if (!defined $number) {
	$number = <STDIN>;
	chomp $number;
}

if (!defined $number || $number !~ /^\d+$/ || $number < 0) {
	usage();
}

my $factorial = 1;

for (my $i = 1; $i <= $number; $i++) {
	$factorial = $factorial * $i;
}

print "$factorial\n";

sub usage {
	print "Usage: please input a non-negative integer\n";
	exit;
}
```

{% endraw %}

Factorial in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Bharath
- Gabriela Kandová

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).