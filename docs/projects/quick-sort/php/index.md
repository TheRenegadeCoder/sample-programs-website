---
title: Quick Sort in Php
layout: default
date: 2019-10-16
featured-image: quick-sort-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if (empty($argv[1])) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$numbers = array_map('intval', explode(',', $argv[1]));
$array_size = count($numbers);

if ($array_size <= 1) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

function quicksort($array)
{
    if (count($array) == 0) {
        return array();
    }

    $pivot_element = $array[0];
    $left_element = $right_element = array();

    for ($i = 1; $i < count($array); $i++) {
        if ($array[$i] < $pivot_element) {
            $left_element[] = $array[$i];
        } else {
            $right_element[] = $array[$i];
        }

    }

    return array_merge(quicksort($left_element), array($pivot_element), quicksort($right_element));
}

$sorted_numbers = quicksort($numbers);

echo implode(', ', $sorted_numbers);
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Php](https://sampleprograms.io/languages/php) was written by:

- Gurmeet
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Oct 16 2019 00:10:51. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).