---
authors:
- Tim W
- Ștefan-Iulian Alecu
date: 2025-02-13
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- linear-search
- perl
title: Linear Search in Perl
title1: Linear Search
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/perl/how-to-implement-the-solution.md
- sources/programs/linear-search/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](/projects/linear-search) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

use feature qw/keyword_any/;
no warnings 'experimental::keyword_any';

sub usage {
    say 'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")';
    exit;
}

sub parse_list ($s) {
    return undef unless defined $s;

    my @vals = split /\s*,\s*/, $s;

    return undef unless @vals;
    return undef if any { $_ !~ /\A\d+\z/ } @vals;

    @vals = map 0 + $_, @vals;

    return \@vals;
}

my ( $list_s, $num_s ) = @ARGV;

defined $num_s or usage();

my $list = parse_list($list_s) or usage();

usage() unless $num_s =~ /\A\d+\z/;
my $num = 0 + $num_s;

my $found = any { $_ == $num } @$list;
say $found ? "true" : "false";

```

{% endraw %}

Linear Search in [Perl](/languages/perl) was written by:

- Tim W
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).