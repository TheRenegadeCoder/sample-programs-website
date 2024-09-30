---
authors:
- Gurmeet
- Jeremy Grifski
date: 2019-10-16
featured-image: selection-sort-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- php
- selection-sort
title: Selection Sort in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/php/how-to-implement-the-solution.md
- sources/programs/selection-sort/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

function selection_sort($data)
{
    for ($i = 0; $i < count($data) - 1; $i++) {
        $min = $i;
        for ($j = $i + 1; $j < count($data); $j++) {
            if ($data[$j] < $data[$min]) {
                $min = $j;
            }
        }
        $data = swap_positions($data, $i, $min);
    }
    return $data;
}

function swap_positions($data1, $left, $right)
{
    $backup = $data1[$right];
    $data1[$right] = $data1[$left];
    $data1[$left] = $backup;
    return $data1;
}

echo implode(', ', selection_sort($numbers));

```

{% endraw %}

Selection Sort in [Php](https://sampleprograms.io/languages/php) was written by:

- Gurmeet
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).