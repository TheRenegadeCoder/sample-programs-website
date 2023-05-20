---
title: Rot13 in Perl
layout: default
date: 2019-10-30
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-30

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
my ($str) = @ARGV;


if (not defined $str or not length $str) {
    die "Usage: please provide a string to encrypt\n";
}

$str =~ tr/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm/;
print $str . "\n";
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Gijs Hendriksen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).