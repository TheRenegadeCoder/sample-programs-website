---
authors:
- SourabhBadhya
- Ștefan-Iulian Alecu
date: 2020-10-02
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- bubble-sort
- perl
title: Bubble Sort in Perl
title1: Bubble Sort
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/perl/how-to-implement-the-solution.md
- sources/programs/bubble-sort/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](/projects/bubble-sort) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

sub bubble_sort ($a) {
    my $n = @$a;

    for my $end ( reverse 1 .. $n - 1 ) {
        my $swapped = false;

        for my $i ( 0 .. $end - 1 ) {
            next if $a->[$i] <= $a->[ $i + 1 ];
            ( $a->[$i], $a->[ $i + 1 ] ) = ( $a->[ $i + 1 ], $a->[$i] );
            $swapped = true;
        }

        last unless $swapped;
    }

    return $a;
}

my ($input) = @ARGV;
my $a = parse_list($input) or usage();

bubble_sort($a);
say join ', ', @$a;

```

{% endraw %}

Bubble Sort in [Perl](/languages/perl) was written by:

- SourabhBadhya
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).