---
authors:
- Jeremy Grifski
date: 2018-09-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2022-05-09
layout: default
tags:
- fizz-buzz
- php
title: Fizz Buzz in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/php/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

for ($i = 1; $i < 101; $i++) {
    $output = "";

    if ($i % 3 == 0) {
        $output .= "Fizz";
    }

    if ($i % 5 == 0) {
        $output .= "Buzz";
    }

    if (!$output) {
        $output = $i;
    }

    echo $output . "\n";
}

```

{% endraw %}

Fizz Buzz in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).