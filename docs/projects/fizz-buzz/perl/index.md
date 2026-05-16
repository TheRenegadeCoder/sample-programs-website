---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2019-03-25
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-05-14
layout: default
tags:
- fizz-buzz
- perl
title: Fizz Buzz in Perl
title1: Fizz Buzz
title2: in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/perl/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;

sub fizzbuzz ($n) {
    my $s = '';

    $s .= "Fizz" if $n % 3 == 0;
    $s .= "Buzz" if $n % 5 == 0;

    return $s || $n;
}

say fizzbuzz($_) for 1 .. 100;

```

{% endraw %}

Fizz Buzz in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).