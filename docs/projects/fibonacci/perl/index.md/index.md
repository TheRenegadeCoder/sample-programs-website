---

---

Welcome to the Fibonacci in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Perl
#!/usr/bin/perl
$num_args = $#ARGV + 1;
if ($num_args == 0) {
    print "Usage: please input the count of fibonacci numbers to output\n";
} elsif ($num_args == 1) {
    if ($ARGV[0] =~ /[0-9]+/) {
    	$n = $ARGV[0];
	$result = 0,$first = 0,$second = 1;
	for ($i = 1;$i <= $n;$i = $i + 1) {
	    $result = $first + $second;
	    $first = $second;
	    $second = $result;
	    print "$i: $first\n";
    	}
    } else {
        print "Usage: please input the count of fibonacci numbers to output\n";    
    }
} else {
    print "Usage: please input the count of fibonacci numbers to output\n";	
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.