---
authors:
- Meet Thakur
date: 2025-10-11
featured-image: binary-search-in-every-language.jpg
last-modified: 2025-10-11
layout: default
tags:
- binary-search
- perl
title: Binary Search in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/perl/how-to-implement-the-solution.md
- sources/programs/binary-search/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

sub handle_error {
    print "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n";
    exit(0);
}

sub check {
    my ($s) = @_;
    
    # Trim leading and trailing spaces
    $s =~ s/^\s+//;
    $s =~ s/\s+$//;
    
    # Check if there are spaces in the middle
    if ($s =~ /\s/) {
        handle_error();
    }
    
    # Check if it's a valid integer
    if ($s !~ /^-?\d+$/) {
        handle_error();
    }
    
    return int($s);
}

sub convert {
    my ($s) = @_;
    
    if (length($s) == 0) {
        handle_error();
    }
    
    my @v;
    my @parts = split(',', $s);
    
    foreach my $part (@parts) {
        push @v, check($part);
    }
    
    return @v;
}

# Main program
if (@ARGV < 2) {
    handle_error();
}

my @v = convert($ARGV[0]);
my $num = check($ARGV[1]);

# Check if array is sorted
for (my $i = 0; $i < @v - 1; $i++) {
    if ($v[$i] > $v[$i + 1]) {
        handle_error();
    }
}

# Binary search
my $start = 0;
my $end = scalar(@v);
my $ans = "false";

while ($start < $end) {
    my $mid = int(($start + $end) / 2);
    
    if ($num < $v[$mid]) {
        $end = $mid;
    }
    elsif ($v[$mid] < $num) {
        $start = $mid + 1;
    }
    elsif ($v[$mid] == $num) {
        $ans = "true";
        last;
    }
}

print "$ans\n";
```

{% endraw %}

Binary Search in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).