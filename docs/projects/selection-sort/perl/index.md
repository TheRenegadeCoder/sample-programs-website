---
authors:
- Mr Anand Somashekhara Rao Somavarapete
date: 2023-10-03
featured-image: selection-sort-in-every-language.jpg
last-modified: 2023-10-03
layout: default
tags:
- perl
- selection-sort
title: Selection Sort in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/perl/how-to-implement-the-solution.md
- sources/programs/selection-sort/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/perl
#Selection Sort
$num_args = $#ARGV + 1;
# If no input was provided
if ($num_args == 0) {
    print "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
} 
# If invalid input was provided
else {
    $input_string = $ARGV[0];
    my @arr = split(',',$input_string);
    $n = $#arr + 1;
    if ($n <= 1) {
	print "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
    } 
#Input is fine    
    else {
# Convert input sting to Integers
        for ($i = 0;$i < $n;$i++) {
                $arr[$i] = int($arr[$i])
            } #end for

@selection_sorted_list = selection_sort (@arr);

# Print sorted numbers
        for ($i = 0;$i < $n;$i = $i + 1) {
            if ($i == 0) {
                print "$selection_sorted_list[$i]";
            } else {
                print ", $selection_sorted_list[$i]";
            }
        }
    }
}

sub selection_sort
  {my @a = @_;
   foreach my $i (0 .. $#a - 1)
      {my $min = $i + 1;
       $a[$_] < $a[$min] and $min = $_ foreach $min .. $#a;
       $a[$i] > $a[$min] and @a[$i, $min] = @a[$min, $i];}
   return @a;}

```

{% endraw %}

Selection Sort in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Mr Anand Somashekhara Rao Somavarapete

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).