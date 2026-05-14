---
authors:
- Kateryna Tokar
- Ștefan-Iulian Alecu
date: 2019-10-23
featured-image: baklava-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- baklava
- perl
title: Baklava in Perl
title1: Baklava
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/perl/how-to-implement-the-solution.md
- sources/programs/baklava/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

my $size = 10;

for my $i ( -$size .. $size ) {
    my $spaces = abs($i);
    my $stars  = 2 * ( $size - $spaces ) + 1;

    say ' ' x $spaces, '*' x $stars;
}

```

{% endraw %}

Baklava in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Kateryna Tokar
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).