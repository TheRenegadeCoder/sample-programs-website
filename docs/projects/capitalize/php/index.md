---
authors:
- Dowayne Breedt
- Jeremy Grifski
date: 2019-10-12
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- php
title: Capitalize in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/php/how-to-implement-the-solution.md
- sources/programs/capitalize/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if (count($argv) == 2 && strlen($argv[1])) {
    $inputString = $argv[1];
    $capitalized = ucfirst($inputString);
    echo $capitalized;
} else {
    echo "Usage: please provide a string";
}

```

{% endraw %}

Capitalize in [Php](https://sampleprograms.io/languages/php) was written by:

- Dowayne Breedt
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).