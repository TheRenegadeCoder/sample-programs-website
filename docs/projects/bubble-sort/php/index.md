---
authors:
- Jeremy Grifski
- Parker Johansen
- Shahab Rahnama
date: 2019-10-04
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- bubble-sort
- php
title: Bubble Sort in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/php/how-to-implement-the-solution.md
- sources/programs/bubble-sort/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

for ($i = 0; $i < $array_size; $i++) {
    for ($j = 0; $j < $array_size; $j++) {
        if ($numbers[$i] < $numbers[$j]) {
            $temp = $numbers[$i];
            $numbers[$i] = $numbers[$j];
            $numbers[$j] = $temp;
        }
    }
}

echo implode(', ', $numbers);

```

{% endraw %}

Bubble Sort in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Parker Johansen
- Shahab Rahnama

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).