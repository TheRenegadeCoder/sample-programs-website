---

title: Fizz Buzz in Perl

---

Welcome to the Fizz Buzz in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Perl
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.