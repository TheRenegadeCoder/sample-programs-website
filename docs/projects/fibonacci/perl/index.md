---
title: Fibonacci in Perl
layout: default
date: 2020-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
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

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- SourabhBadhya

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).