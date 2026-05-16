---
authors:
- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu
date: 2023-10-03
featured-image: selection-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- perl
- selection-sort
title: Selection Sort in Perl
title1: Selection
title2: Sort in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/perl/how-to-implement-the-solution.md
- sources/programs/selection-sort/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

sub selection_sort ($a) {
    my $n = @$a;

    for my $i ( 0 .. $n - 2 ) {
        my $min = $i;

        for my $j ( $i + 1 .. $n - 1 ) {
            $min = $j if $a->[$j] < $a->[$min];
        }

        ( $a->[$i], $a->[$min] ) = ( $a->[$min], $a->[$i] ) if $i != $min;
    }

    return $a;
}

my ($input) = @ARGV;
my $a = parse_list($input) or usage();

selection_sort($a);
say join ', ', @$a;

```

{% endraw %}

Selection Sort in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).