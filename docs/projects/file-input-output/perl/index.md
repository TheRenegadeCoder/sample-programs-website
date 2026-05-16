---
authors:
- Ewerton Queiroz
- Ștefan-Iulian Alecu
date: 2019-10-15
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- file-input-output
- perl
title: File Input Output in Perl
title1: File Input
title2: Output in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/perl/how-to-implement-the-solution.md
- sources/programs/file-input-output/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Perl](https://sampleprograms.io/languages/perl)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use v5.42;
use IO::File;

my $file    = "output.txt";
my $content = <<'EOF';
Perl is cool!
There's more than one way to do it.
EOF

# Write to file

my $w = IO::File->new(">$file") or die "Cannot open $file for writing: $!";
$w->print($content)             or die "Write failed: $!";
$w->close                       or die "Cannot close after write: $!";

# Read from file

my $r = IO::File->new("<$file") or die "Cannot open $file for reading: $!";
print while <$r>;
$r->close or die "Cannot close after read: $!";

```

{% endraw %}

File Input Output in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Ewerton Queiroz
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).