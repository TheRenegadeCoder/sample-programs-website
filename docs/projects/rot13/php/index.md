---
authors:
- Andy Alban
- Jeremy Grifski
date: 2019-10-13
featured-image: rot13-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- php
- rot13
title: Rot13 in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/php/how-to-implement-the-solution.md
- sources/programs/rot13/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if (empty($argv[1]) || $argv[1] == "" || count($argv) == 0) {
    die("Usage: please provide a string to encrypt\n");
}

function rot13(string $string)
{
    return strtr($string,
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm');
}

echo rot13($argv[1]) . "\n";

```

{% endraw %}

Rot13 in [Php](https://sampleprograms.io/languages/php) was written by:

- Andy Alban
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).