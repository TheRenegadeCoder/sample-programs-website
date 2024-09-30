---
authors:
- Jeremy Grifski
- Parker Johansen
- sljtheultima
date: 2019-10-13
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- insertion-sort
- php
title: Insertion Sort in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/php/how-to-implement-the-solution.md
- sources/programs/insertion-sort/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

function insertion_Sort($my_array)
{
    for ($i = 0; $i < count($my_array); $i++) {
        $val = $my_array[$i];
        $j = $i - 1;
        while ($j >= 0 && $my_array[$j] > $val) {
            $my_array[$j + 1] = $my_array[$j];
            $j--;
        }
        $my_array[$j + 1] = $val;
    }
    return $my_array;
}

if (empty($argv[1])) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$test_array = array_map('intval', explode(',', $argv[1]));
$array_size = count($test_array);

if ($array_size <= 1) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$out = insertion_Sort($test_array);
echo implode(', ', $out);

```

{% endraw %}

Insertion Sort in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Parker Johansen
- sljtheultima

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).