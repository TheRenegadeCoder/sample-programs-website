---
authors:
- Chris Thomas
- Jeremy Grifski
date: 2018-10-12
featured-image: fizz-buzz-in-every-language.png
last-modified: 2019-03-25
layout: default
tags:
- fizz-buzz
- perl
title: Fizz Buzz in Perl
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
#!/usr/bin/perl
#
# FizzBuzz in Perl

use strict;
use warnings;
use diagnostics;
use 5.10.0;

for my $n (1..100) {
    !($n % 15) ?    say "FizzBuzz"    :
    !($n % 3)  ?    say "Fizz"        :
    !($n % 5)  ?    say "Buzz"        :
                    say "$n";
}

```

{% endraw %}

Fizz Buzz in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Chris Thomas
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).