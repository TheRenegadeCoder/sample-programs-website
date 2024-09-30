---
authors:
- Ewerton Queiroz
date: 2019-10-15
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-15
layout: default
tags:
- file-input-output
- perl
title: File Input Output in Perl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/perl/how-to-implement-the-solution.md
- sources/programs/file-input-output/perl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl

sub Main {
	Write("Some arbitrary data.");
	Read();
	exit(0);
}

sub Write {
	open(my $writing, ">output.txt") || die "File could not be written.\nError: $!";

	print $writing "@_"."\n";

	close($writing) || die "The file could not be closed on write.\nError: $!";
}

sub Read {
	open(my $reading, "<output.txt") || die "File could not be readed.\nError: $!";

	while (!eof($reading)) {
		print <$reading>;
	}

	close($reading) || die "The file could not be closed on reading.\nError: $!";
}

Main();

```

{% endraw %}

File Input Output in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Ewerton Queiroz

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).