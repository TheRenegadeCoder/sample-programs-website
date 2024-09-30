---
authors:
- rzuckerm
date: 2023-03-23
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-03-27
layout: default
tags:
- longest-word
- php
title: Longest Word in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/php/how-to-implement-the-solution.md
- sources/programs/longest-word/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please provide a string");
}

function longest_word_length($str)
{
    // Split on whitespace, get string length of each word, take the maximum
    return max(array_map("strlen", preg_split("/\s+/", $str)));
}

// Exit if too few arguments or 1st command-line argument is empty
if (count($argv) < 2 || empty($argv[1]))
{
    usage();
}

// Get longest word length and display
$str = $argv[1];
$longest_len = longest_word_length($str);
echo "${longest_len}\n";

```

{% endraw %}

Longest Word in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).