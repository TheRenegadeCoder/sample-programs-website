---
authors:
- rzuckerm
date: 2023-03-23
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-03-23
layout: default
tags:
- php
- remove-all-whitespace
title: Remove All Whitespace in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/php/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please provide a string");
}

function remove_all_whitespace($str)
{
    return preg_replace("/\s+/", "", $str);
}

// Exit if too few arguments or 1st argument is empty
if (count($argv) < 2 || empty($argv[1]))
{
    usage();
}

// Remove all whitespace and display string
$str = remove_all_whitespace($argv[1]);
echo "${str}\n";

```

{% endraw %}

Remove All Whitespace in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).