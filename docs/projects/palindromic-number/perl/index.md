---
authors:
- manasmithamn
- Ștefan-Iulian Alecu
date: 2021-10-29
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- palindromic-number
- perl
title: Palindromic Number in Perl
title1: Palindromic
title2: Number in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/perl/how-to-implement-the-solution.md
- sources/programs/palindromic-number/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
say $n eq reverse($n) ? "true" : "false";

```

{% endraw %}

Palindromic Number in [Perl](https://sampleprograms.io/languages/perl) was written by:

- manasmithamn
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).