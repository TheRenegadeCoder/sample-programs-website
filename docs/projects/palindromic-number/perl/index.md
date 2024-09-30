---
authors:
- Jeremy Grifski
- manasmithamn
date: 2021-10-29
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2022-10-11
layout: default
tags:
- palindromic-number
- perl
title: Palindromic Number in Perl
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

# accept an integer, reverse it, compare it with original
# print true, if original and reversed number are same
# print false, if original and reversed number are same
#!/usr/bin/env perl
use strict;
use warnings;

# no input
usage() unless @ARGV == 1;

# accept input as argument
my ($number) = @ARGV;

# if not provided, read from standard input
if (!defined $number) {
	$number = <STDIN>;
	chomp $number;
}

if (!defined $number || $number !~ /^\d+$/ || $number < 0) {
	usage();
}

my $temp = $number;
my $noofdigits = 0;
my $reversed_number = 0;
while ($temp > 0){
  $reversed_number = ($reversed_number * 10) + ($temp % 10);
  $temp = int($temp / 10);
  $noofdigits += 1;
}

if ($number < 0){
  print("Usage: please input a non-negative integer")
}

else{
  if ($reversed_number == $number){
    print("true");
    }
  else{
    print("false");
  }

}

sub usage {
	print "Usage: please input a non-negative integer";
	exit;
}

```

{% endraw %}

Palindromic Number in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Jeremy Grifski
- manasmithamn

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).