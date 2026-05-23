---
authors:
- Mallikarjuna S J
- Ștefan-Iulian Alecu
date: 2019-10-31
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- perl
- prime-number
title: Prime Number in Perl
title1: Prime Number
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/perl/how-to-implement-the-solution.md
- sources/programs/prime-number/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](/projects/prime-number) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

sub usage {
    say "Usage: please input a non-negative integer";
    exit;
}

my ($n) = @ARGV;
usage() unless defined $n && $n =~ /\A\d+\z/;

$n += 0;

say "Composite" and exit if $n < 2;
say "Prime"     and exit if $n == 2;
say "Composite" and exit if $n % 2 == 0;

for ( my $i = 3 ; $i * $i <= $n ; $i += 2 ) {
    say "Composite" and exit if $n % $i == 0;
}

say "Prime";

```

{% endraw %}

Prime Number in [Perl](/languages/perl) was written by:

- Mallikarjuna S J
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).