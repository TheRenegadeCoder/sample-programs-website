---
authors:
- "Gabriela Kandov\xE1"
- Jeremy Grifski
date: 2019-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- perl
title: Capitalize in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/perl/how-to-implement-the-solution.md
- sources/programs/capitalize/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

# accept input as argument
my ($string) = @ARGV;

if (!defined $string || length $string == 0) {
	print "Usage: please provide a string\n";
	exit;
}

print ucfirst $string, "\n";

```

{% endraw %}

Capitalize in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Gabriela Kandová
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).