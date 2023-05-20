---
title: Even Odd in Php
layout: default
date: 2019-10-16
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if ($argc < 2 || !is_numeric($argv[1])) {
    die("Usage: please input a number\n");
}

$input = abs($argv[1]);

if ($input % 2 == 0) {
    echo "Even\n";
} elseif ($input % 2 == 1) {
    echo "Odd\n";
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Php](https://sampleprograms.io/languages/php) was written by:

- Berry Semexan
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Oct 16 2019 23:28:43. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).