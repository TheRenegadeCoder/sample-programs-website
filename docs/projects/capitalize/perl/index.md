---
authors:
- Gabriela Kandová
- Ștefan-Iulian Alecu
date: 2019-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- capitalize
- perl
title: Capitalize in Perl
title1: Capitalize
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/perl/how-to-implement-the-solution.md
- sources/programs/capitalize/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](/projects/capitalize) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

sub usage {
    say "Usage: please provide a string";
    exit;
}

my ($string) = @ARGV;
usage() unless defined $string && length $string;

say ucfirst $string;

```

{% endraw %}

Capitalize in [Perl](/languages/perl) was written by:

- Gabriela Kandová
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).