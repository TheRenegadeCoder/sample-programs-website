---
title: Capitalize in Perl
layout: default
date: 2019-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-17

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

# accept input as argument
my ($string) = @ARGV;

if (!defined $string || length $string == 0) {
    print "Usage: please provide a string\n";
    exit;
}

print ucfirst $string, "\n";
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Gabriela Kandová
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 20:37:32. The solution was first committed on Oct 17 2019 11:06:11. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).