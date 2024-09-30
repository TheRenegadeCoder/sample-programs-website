---
authors:
- Jeremy Grifski
- Juan D Frias
- Parker Johansen
date: 2019-10-14
featured-image: prime-number-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- php
- prime-number
title: Prime Number in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/php/how-to-implement-the-solution.md
- sources/programs/prime-number/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

/**
 * Function to determine if a number if prime.
 * @param int positive integer.
 * @return True if the number is prime, False otherwise.
 */
function is_prime($num)
{
    if (($num % 2 == 0 && $num != 2) || ($num == 1)) {
        return false;
    }

    $found_factor = false;
    for ($n = 3; $n <= intval(ceil(sqrt($num))); ++$n) {
        if (($num % $n) == 0) {
            $found_factor = true;
            break;
        }
    }

    return !$found_factor;
}

// Check argument
if ($argc < 2 || !is_numeric($argv[1]) || strpos($argv[1], '.') !== false || strpos($argv[1], '-') !== false) {
    echo "Usage: please input a non-negative integer\n";
    exit(1);
}

// Convert the string
if (is_prime(intval($argv[1]))) {
    echo "Prime\n";

} else {
    echo "Composite\n";
}

exit(0);

```

{% endraw %}

Prime Number in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Juan D Frias
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).