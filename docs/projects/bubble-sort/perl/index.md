---

title: Bubble Sort in Perl
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Bubble Sort in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Perl
#!/usr/bin/perl
$num_args = $#ARGV + 1;
if ($num_args == 0) {
    print "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
} else {
    $input_string = $ARGV[0];
    my @arr = split(',',$input_string);
    $n = $#arr + 1;
    if ($n <= 1) {
	print "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
    } else {
	for ($i = 0;$i < $n;$i++) {
	    $arr[$i] = int($arr[$i])
	}
        for ($i = 0;$i < $n;$i = $i + 1) {
            for ($j = 0;$j < $n - $i - 1;$j = $j + 1) {
                if ($arr[$j] > $arr[$j + 1]) {
                    $temp = $arr[$j];
                    $arr[$j] = $arr[$j + 1];
                    $arr[$j + 1] = $temp;
                }
            }
        }
        for ($i = 0;$i < $n;$i = $i + 1) {
            if ($i == 0) {
                print "$arr[$i]";
            } else {
                print ", $arr[$i]";
            }
        }
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.