---
authors:
- rzuckerm
date: 2023-03-27
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2023-03-27
layout: default
tags:
- maximum-subarray
- php
title: Maximum Subarray in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/php/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit('Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"');
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

function parse_int_array($str_values)
{
    $str_array = explode(",", $str_values);
    $values = array();
    foreach ($str_array as $str_value)
    {
        $value = parse_int($str_value);
        if ($value === FALSE)
        {
            return FALSE;
        }

        array_push($values, $value);
    }

    return $values;
}

// Find maximum subarray using Kadane's algorithm.
// Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted
function maximum_subarray($values)
{
    $best_sum = PHP_INT_MIN;
    $current_sum = 0;
    foreach ($values as $value)
    {
        $current_sum = $value + max(0, $current_sum);
        $best_sum = max($best_sum, $current_sum);
    }

    return $best_sum;
}

// Exit if too few arguments
if (count($argv) < 2)
{
    usage();
}

// Parse 1st command-line argument. Exit if invalid
$values = parse_int_array($argv[1]);
if ($values === FALSE)
{
    usage();
}

// Calculate maximum subarray and display
$max_value = maximum_subarray($values);
echo "${max_value}\n";

```

{% endraw %}

Maximum Subarray in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).