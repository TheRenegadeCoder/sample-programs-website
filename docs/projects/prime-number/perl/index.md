---
authors:
- Mallikarjuna S J
date: 2019-10-31
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-11-05
layout: default
tags:
- perl
- prime-number
title: Prime Number in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/perl/how-to-implement-the-solution.md
- sources/programs/prime-number/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
# Requirement https://sample-programs.therenegadecoder.com/projects/prime-number/
# Issue  #1834
# Accept a number on command line and print if it is Prime or Composite
# Prime Numbers will have only 1 Divisor, itself..  Use that to determine Composite.
# Note: 0 and 1 are Composite numbers, 2 is a Prime Number
use warnings;

my ($prime) = @ARGV;

$num_args = $#ARGV + 1;

# Empty input
if ( $num_args < 1 ) {
    print("Usage: please input a non-negative integer");
    exit(0);
}

# Only Integer
if ( $prime =~ /^-?\d+$/ ) {

    # Negative Number
    if ( $prime < 0 ) {
        print("Usage: please input a non-negative integer");
        exit(0);
    }

    if ( $prime == 2 ) {
        print("Prime");
        exit(0);
    }

    # If 1 or the Number is Even
    elsif ( ( $prime == 1 ) || ( $prime == 0 ) || ( $prime % 2 == 0 ) ) {
        print("Composite");
        exit(0);
    }

    else {
        #   Check how many divisors for the given number
        $i               = 0;
        $num_of_divisors = 0;

        #   Number is guaranteed to be Even
        for ( $i = $prime ; $i > 1 ; $i = $i - 2 ) {
            if ( $prime % $i == 0 ) {
                $num_of_divisors += 1;
            }
        }

        # If more than 2 divisors
        if ( $num_of_divisors > 2 ) {
            print("Composite");
        }
        else {
            print("Prime");
        }
    }

}

# If not Integer
else {
    print "Usage: please input a non-negative integer";
    exit(0);
}

```

{% endraw %}

Prime Number in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).