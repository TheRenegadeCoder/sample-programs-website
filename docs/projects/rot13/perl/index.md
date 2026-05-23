---
authors:
- Gijs Hendriksen
- Ștefan-Iulian Alecu
date: 2019-10-30
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- perl
- rot13
title: Rot13 in Perl
title1: Rot13
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/perl/how-to-implement-the-solution.md
- sources/programs/rot13/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](/projects/rot13) in [Perl](/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

sub usage {
    say "Usage: please provide a string to encrypt";
    exit;
}

my ($str) = @ARGV;
usage() unless defined $str && length $str;

$str =~ tr/A-Za-z/N-ZA-Mn-za-m/;
say $str;

```

{% endraw %}

Rot13 in [Perl](/languages/perl) was written by:

- Gijs Hendriksen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).