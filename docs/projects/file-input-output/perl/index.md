---
title: File Input Output in Perl
layout: default
date: 2019-10-15
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-15

---

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

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Ewerton Queiroz

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2019 01:29:31. The solution was first committed on Oct 15 2019 01:15:38. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).