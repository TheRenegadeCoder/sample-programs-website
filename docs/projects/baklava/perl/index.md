---
title: Baklava in Perl
layout: default
date: 2019-10-23
featured-image: baklava-in-every-language.jpg
last-modified: 2019-10-23

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/env perl
use strict;
use warnings;

my $size = 10;

for my $i (1..$size){
    print " "x($size + 1 - $i), "*"x($i*2 - 1), "\n";
}

for my $j (0..$size){
    print " "x($j), "*"x($size*2 - $j*2 + 1), "\n";
}
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Kateryna Tokar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).