---

---

# Factorial in Perl

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Perl
#!/usr/bin/env perl
use strict;
use warnings;

# no input
usage() unless @ARGV == 1;

# accept input as argument
my ($number) = @ARGV;

# if not provided, read from standard input
if (!defined $number) {
	$number = <STDIN>;
	chomp $number;
}

if (!defined $number || $number !~ /^\d+$/ || $number < 0) {
	usage();
}

my $factorial = 1;

for (my $i = 1; $i <= $number; $i++) {
	$factorial = $factorial * $i;
}

print "$factorial\n";

sub usage {
	print "Usage: please input a non-negative integer\n";
	exit;
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.