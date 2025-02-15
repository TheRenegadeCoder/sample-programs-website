---
authors:
- rzuckerm
date: 2023-03-21
featured-image: binary-search-in-every-language.jpg
last-modified: 2023-03-27
layout: default
tags:
- binary-search
- php
title: Binary Search in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/php/how-to-implement-the-solution.md
- sources/programs/binary-search/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit('Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")');
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

function check_sorted($values)
{
    for ($index = 1; $index < count($values); $index++)
    {
        if ($values[$index - 1] > $values[$index]) {
            return FALSE;
        }
    }

    return TRUE;
}

function binary_search($target, $values)
{
    $low = 0;
    $high = count($values);
    while ($low < $high)
    {
        $mid = intdiv($low + $high, 2);

        // If found it, return index
        if ($values[$mid] == $target)
        {
            return $mid;
        }

        // If too low, move lower bound
        if ($values[$mid] < $target)
        {
            $low = $mid + 1;
        }
        // Else, move upper bound
        else
        {
            $high = $mid;
        }
    }

    return -1;
}

// Exit if too few arguments
if (count($argv) < 3)
{
    usage();
}

// Parse 1st argument. Exit if invalid
$values = parse_int_array($argv[1]);
if ($values === FALSE)
{
    usage();
}

// Parse 2nd argument. Exit if invalid
$target = parse_int($argv[2]);
if ($target == FALSE)
{
    usage();
}

// Make sure list is sorted
if (!check_sorted($values))
{
    usage();
}

// Do binary search and show results
$index = binary_search($target, $values);
printf("%s\n", ($index >= 0) ? "true" : "false");
?>

```

{% endraw %}

Binary Search in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).