---
authors:
- rzuckerm
date: 2023-03-24
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2023-03-24
layout: default
tags:
- josephus-problem
- php
title: Josephus Problem in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/php/how-to-implement-the-solution.md
- sources/programs/josephus-problem/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please input the total number of people and number of people to skip.");
}

function parse_int($str_value)
{
    // Remove leading and trailing spaces
    $str_value = trim($str_value);

    // Make sure all digits
    if (preg_match("/^[+-]?\d+$/", $str_value) === FALSE)
    {
        return FALSE;
    }

    // Make sure valid integer
    if (
        filter_var(
            $str_value,
            FILTER_VALIDATE_INT,
            array(
                'options' => array(
                    'decimal' => TRUE,
                    'min_range' => PHP_INT_MIN,
                    'max_range' => PHP_INT_MAX
                )
            )
        ) === FALSE
    )
    {
        return FALSE;
    }

    return intval($str_value);
}

// Reference: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
//
// Use zero-based index algorithm:
//
//    g(1, k) = 0
//    g(m, k) = [g(m - 1, k) + k] MOD m, for m = 2, 3, ..., n
//
// Final answer is g(n, k) + 1 to get back to one-based index
function josephus($n, $k)
{
    $g = 0;
    for ($m = 2; $m <= $n; $m++)
    {
        $g = ($g + $k) % $m;
    }

    return $g + 1;
}

// Exit if too few arguments
if (count($argv) < 3)
{
    usage();
}

// Parse arguments. Exit if invalid
$n = parse_int($argv[1]);
$k = parse_int($argv[2]);
if ($n === FALSE || $k === FALSE)
{
    usage();
}

// Run Josephus problem and store results
$g = josephus($n, $k);
echo "${g}\n";

```

{% endraw %}

Josephus Problem in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).