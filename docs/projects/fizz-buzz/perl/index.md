---

title: Fizz Buzz in Perl
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
#!/usr/bin/perl
#
# FizzBuzz in Perl

use strict;
use warnings;
use diagnostics;
use 5.10.0;

for my $n (1..100) {
    !($n % 15) ?    say "FizzBuzz"    :
    !($n % 3)  ?    say "Fizz"        :
    !($n % 5)  ?    say "Buzz"        :
                    say "$n";
}
```

{% endraw %}

Fizz Buzz in Perl was written by:

- Jeremy Grifski
- Chris Thomas

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 25 2019 12:44:48. The solution was first committed on Oct 12 2018 17:15:01. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).