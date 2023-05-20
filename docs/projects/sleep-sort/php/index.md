---
title: Sleep Sort in Php
layout: default
date: 2023-03-21
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2023-03-21

---

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
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

// PHP requires PECL to be install to have threads. However, the docker
// image does not have this. Therefore, just monitor the clock and store
// values as each sleep time elapses
function sleep_sort($sleep_times)
{
    // Initialize values
    $values = array();

    // Wait for all sleep times are complete
    $start = microtime(TRUE);
    while (TRUE)
    {
        // For each sleep time that is not complete, when sleep time expires, append the
        // sleep time to the list of values and remove the sleep time from the list
        $elapsed_time = microtime(TRUE) - $start;
        $new_sleep_times = array();
        foreach ($sleep_times as $sleep_time)
        {
            if ($elapsed_time >= $sleep_time)
            {
                array_push($values, $sleep_time);
            }
            else
            {
                array_push($new_sleep_times, $sleep_time);
            }
        }

        $sleep_times = $new_sleep_times;
        if (count($sleep_times) < 1)
        {
            return $values;
        }

        time_nanosleep(0, 500_000_000);
    }
}

// Exit if too few arguments
if (count($argv) < 2)
{
    usage();
}

// Parse 1st argument. Exit if invalid or too few values
$values = parse_int_array($argv[1]);
if ($values === FALSE || count($values) < 2)
{
    usage();
}

// Run sleep sort and show results
$values = sleep_sort($values);
printf("%s\n", implode(", ", $values));
```

{% endraw %}

[Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 24 2023 20:24:38. The solution was first committed on Mar 21 2023 00:04:47. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).