---

title: Factorial in Perl
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Factorial in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```perl
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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).