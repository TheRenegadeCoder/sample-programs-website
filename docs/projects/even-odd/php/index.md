---
authors:
- Berry Semexan
- Jeremy Grifski
date: 2019-10-16
featured-image: even-odd-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- even-odd
- php
title: Even Odd in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/php/how-to-implement-the-solution.md
- sources/programs/even-odd/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if ($argc < 2 || !is_numeric($argv[1])) {
    die("Usage: please input a number\n");
}

$input = abs($argv[1]);

if ($input % 2 == 0) {
    echo "Even\n";
} elseif ($input % 2 == 1) {
    echo "Odd\n";
}

```

{% endraw %}

Even Odd in [Php](https://sampleprograms.io/languages/php) was written by:

- Berry Semexan
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).