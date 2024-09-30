---
authors:
- Carles Capell
- Parker Johansen
date: 2019-01-03
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-15
layout: default
tags:
- fibonacci
- php
title: Fibonacci in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/php/how-to-implement-the-solution.md
- sources/programs/fibonacci/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if ($argc < 2 || !is_numeric($argv[1]) || intval($argv[1]) < 0) {
    die("Usage: please input the count of fibonacci numbers to output");
}

$input = intval($argv[1]);

$a = 0;
$b = 1;
$fibonacci = 0;

for ($index = 1; $index <= $input; $index++) {
    $fibonacci = $a + $b;
    $a = $b;
    $b = $fibonacci;
    echo "$index: $a\n";
}
```

{% endraw %}

Fibonacci in [Php](https://sampleprograms.io/languages/php) was written by:

- Carles Capell
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).