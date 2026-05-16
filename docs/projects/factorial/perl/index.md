---
authors:
- Gabriela Kandová
- Ștefan-Iulian Alecu
date: 2019-10-14
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- factorial
- perl
title: Factorial in Perl
title1: Factorial
title2: in Perl
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
use v5.42;

sub usage {
    say "Usage: please input a non-negative integer";
    exit;
}

my ($number) = @ARGV;
usage() unless defined $number && $number =~ /\A\d+\z/;

my $factorial = 1;
$factorial *= $_ for 2 .. $number;

say $factorial;

```

{% endraw %}

Factorial in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Gabriela Kandová
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).