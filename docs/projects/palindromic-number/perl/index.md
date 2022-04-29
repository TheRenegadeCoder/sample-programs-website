---

title: Palindromic Number in Perl

---

Welcome to the Palindromic Number in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Perl

# accept an integer, reverse it, compare it with original
# print true, if original and reversed number are same
# print false, if original and reversed number are same
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

my $temp = $number;
my $noofdigits = 0;
my $reversed_number = 0;
while ($temp > 0){
  $reversed_number = ($reversed_number * 10) + ($temp % 10);
  $temp = int($temp / 10);
  $noofdigits += 1;
}

if ($noofdigits < 2){
  print("Usage: please input a number with at least two digits")
}

else{
  if ($reversed_number == $number){
    print("true");
    }
  else{
    print("false");
  }

}

sub usage {
	print "Usage: please input a number with at least two digits";
	exit;
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.