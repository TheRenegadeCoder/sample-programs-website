---
authors:
- Tim W
date: 2025-02-13
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-02-13
layout: default
tags:
- linear-search
- perl
title: Linear Search in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/perl/how-to-implement-the-solution.md
- sources/programs/linear-search/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/perl
my $arguments_used = scalar @ARGV;
if($arguments_used < 2)
{
    die "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n";
}
my @input_array = @ARGV;
my $input_string = pop @ARGV;
my @trimmed_string = split(',', @input_array[0]);
my $found_it = 0;
if(scalar@trimmed_string < 1)
{
    die "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n";
}
for(my $i = 0; $i < scalar(@trimmed_string); $i++)
{
    if($trimmed_string[$i] == $input_string)
    {
        $found_it = 1;
    }
}
print $found_it ? "true" : "false";
```

{% endraw %}

Linear Search in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Tim W

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).