---
authors:
- Italo Sousa
- Jeremy Grifski
date: 2019-10-10
featured-image: factorial-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- factorial
- php
title: Factorial in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/php/how-to-implement-the-solution.md
- sources/programs/factorial/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

$input = null;
if (
    sizeof($argv) < 2 ||
    !is_numeric($argv[1]) ||
    intval($argv[1]) < 0
) {
    echo ("Usage: please input a non-negative integer\n");
    exit(0);
}

$factorial = 1;
$input = intval($argv[1]);

for ($x = $input; $x >= 1; $x--) {
    $factorial = $factorial * $x;
}

echo ("$factorial\n");

```

{% endraw %}

Factorial in [Php](https://sampleprograms.io/languages/php) was written by:

- Italo Sousa
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).