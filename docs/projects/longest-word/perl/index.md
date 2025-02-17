---
authors:
- Tim W
date: 2025-02-17
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-02-17
layout: default
tags:
- longest-word
- perl
title: Longest Word in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/perl/how-to-implement-the-solution.md
- sources/programs/longest-word/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/perl
my $args = join(" ", @ARGV);
if($args eq "" || $args eq " ")
{
    die "Usage: please provide a string\n"
}
my $total = 0;
my @storage = split(" ", $args);
foreach my $loop (@storage)
{
    if(length($loop) >= $total)
    {
        $total = length($loop);
    }
}
print $total;

```

{% endraw %}

Longest Word in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Tim W

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).