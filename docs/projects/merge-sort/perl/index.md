---
authors:
- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu
date: 2023-10-03
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- merge-sort
- perl
title: Merge Sort in Perl
title1: Merge Sort
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/perl/how-to-implement-the-solution.md
- sources/programs/merge-sort/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Perl](https://sampleprograms.io/languages/perl)! Here, you'll find the source code for this program as well as a description of how the program works.

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

# Note: Perl's `sort` is implemented via merge sort as of v5.42, so one could use that instead.

sub merge_sort ($a) {
    return $a if @$a <= 1;

    my $mid = @$a >> 1;

    my $left  = [ @{$a}[ 0 .. $mid - 1 ] ];
    my $right = [ @{$a}[ $mid .. $#$a ] ];

    merge_sort($left);
    merge_sort($right);

    @$a = _merge( $left, $right );
    return $a;
}

sub _merge ( $left, $right ) {
    my @out;

    while ( @$left && @$right ) {
        push @out, $left->[0] <= $right->[0]
          ? shift @$left
          : shift @$right;
    }

    push @out, @$left, @$right;

    return @out;
}

my ($input) = @ARGV;
my $a = parse_list($input) or usage();

merge_sort($a);
say join ', ', @$a;

```

{% endraw %}

Merge Sort in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Mr Anand Somashekhara Rao Somavarapete
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).