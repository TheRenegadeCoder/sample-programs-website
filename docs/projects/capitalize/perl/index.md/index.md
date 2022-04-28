---

---

# Capitalize in Perl

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Perl
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.