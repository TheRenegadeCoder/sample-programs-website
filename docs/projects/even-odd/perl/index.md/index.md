---

---

# Even Odd in Perl

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Perl
#!/usr/bin/env perl
use strict;
use warnings;

# accept input as argument
my ($number) = @ARGV;

if (!defined $number || $number !~ /^\-?\d+$/) {
	print "Usage: please input a number\n";
	exit;
}

if ($number % 2 == 0) {
	print "Even\n";
} else {
	print "Odd\n";
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.