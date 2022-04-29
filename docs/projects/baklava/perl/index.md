---

title: Baklava in Perl
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Perl
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.