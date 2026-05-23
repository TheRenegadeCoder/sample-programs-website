---
authors:
- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu
date: 2023-10-01
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- perl
- quick-sort
title: Quick Sort in Perl
title1: Quick Sort
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/perl/how-to-implement-the-solution.md
- sources/programs/quick-sort/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](/projects/quick-sort) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

use feature qw/keyword_any/;
no warnings 'experimental::keyword_any';

sub usage {
    say 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';
    exit;
}

sub parse_list ($s) {
    return undef unless defined $s;

    my @vals = split /\s*,\s*/, $s;

    return undef if @vals < 2;
    return undef if any { $_ !~ /\A-?\d+\z/ } @vals;

    return [ map 0 + $_, @vals ];
}

sub quick_sort ($a) {
    return $a if @$a <= 1;

    my $pivot = $a->[ @$a >> 1 ];

    my @left  = grep { $_ < $pivot } @$a;
    my @mid   = grep { $_ == $pivot } @$a;
    my @right = grep { $_ > $pivot } @$a;

    return [ @{ quick_sort( \@left ) }, @mid, @{ quick_sort( \@right ) } ];
}

my ($input) = @ARGV;
my $a = parse_list($input) or usage();

$a = quick_sort($a);
say join ', ', @$a;

```

{% endraw %}

Quick Sort in [Perl](/languages/perl) was written by:

- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).