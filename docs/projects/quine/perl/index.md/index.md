# Quine in Perl

## Solution

```Perl
$s='$s=%c%s%c;printf($s,39,$s,39,10);%c';printf($s,39,$s,39,10);

```