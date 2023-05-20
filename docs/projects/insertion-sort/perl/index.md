---
title: Insertion Sort in Perl
layout: default
date: 2020-10-02
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
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
        for ($i = 1;$i < $n;$i = $i + 1) {
            $p = $arr[$i];
        $j = $i - 1;
        while($j >= 0 && $arr[$j] > $p) {
        $arr[$j + 1] = $arr[$j];
        $j = $j - 1;
        }
        $arr[$j + 1] = $p;
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

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- SourabhBadhya

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).