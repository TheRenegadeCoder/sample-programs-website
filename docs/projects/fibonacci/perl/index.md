---
authors:
- SourabhBadhya
- Ștefan-Iulian Alecu
date: 2020-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- fibonacci
- perl
title: Fibonacci in Perl
title1: Fibonacci
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/perl/how-to-implement-the-solution.md
- sources/programs/fibonacci/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Perl](https://sampleprograms.io/languages/perl)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

sub usage {
    say "Usage: please input the count of fibonacci numbers to output";
    exit;
}

my ($n) = @ARGV;
usage() unless defined $n && $n =~ /\A\d+\z/;

my ( $a, $b ) = ( 0, 1 );

for my $i ( 1 .. $n ) {
    ( $a, $b ) = ( $b, $a + $b );
    say "$i: $a";
}

```

{% endraw %}

Fibonacci in [Perl](https://sampleprograms.io/languages/perl) was written by:

- SourabhBadhya
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).