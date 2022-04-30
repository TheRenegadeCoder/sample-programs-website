---

title: Rot 13 in Perl
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Rot 13 in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Perl
my ($str) = @ARGV;


if (not defined $str or not length $str) {
    die "Usage: please provide a string to encrypt\n";
}

$str =~ tr/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm/;
print $str . "\n";
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).