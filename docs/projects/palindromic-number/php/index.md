---
title: Palindromic Number in Php
layout: default
date: 2023-03-27
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2023-03-27

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please input a non-negative integer");
}

function parse_int($str_value)
{
    // Remove leading and trailing spaces
    $str_value = trim($str_value);

    // Make sure all digits
    if (preg_match("/[+-]?^\d+$/", $str_value) === FALSE)
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

function is_palindromic_number($value)
{
    // Convert number to string
    $str = "${value}";

    // Check if palindrome
    $len = strlen($str);
    $is_palindrome = TRUE;
    for ($left = 0, $right = $len - 1; $left < $right && $is_palindrome; $left++, $right--)
    {
        $is_palindrome = ($str[$left] == $str[$right]);
    }

    return $is_palindrome;

}

// Exit if too few arguments
if (count($argv) < 2)
{
    usage();
}

// Parse 1st command-line argument and exit if invalid or negative
$value = parse_int($argv[1]);
if ($value === FALSE || $value < 0)
{
    usage();
}

// Check if number is a palindrome and display results
$is_palindrome = is_palindromic_number($value);
printf("%s\n", $is_palindrome ? "true" : "false");
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).