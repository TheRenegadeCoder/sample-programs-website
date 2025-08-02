---
authors:
- rzuckerm
date: 2023-03-22
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-08-02
layout: default
tags:
- duplicate-character-counter
- php
title: Duplicate Character Counter in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/php/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please provide a string");
}

function duplicate_character_counter($str)
{
    // Count number of occurances of each character
    $counts = array();
    $len = strlen($str);
    for ($index = 0; $index < $len; $index++)
    {
        $ch = $str[$index];
        if (!array_key_exists($ch, $counts))
        {
            $counts[$ch] = 0;
        }

        $counts[$ch] += 1;
    }

    return $counts;
}

function show_duplicate_character_counts($counts)
{
    // Show characters that have duplicates and keep track if
    // duplicates found
    $has_dupes = FALSE;
    foreach ($counts as $char => $count)
    {
        if ($count > 1)
        {
            echo "$char: $count\n";
            $has_dupes = TRUE;
        }
    }

    // Indicate if no duplicates found
    if (!$has_dupes)
    {
        echo "No duplicate characters\n";
    }
}

// Get 1st argument. Exit if too few arguments or empty argument
if (count($argv) < 2 || empty($argv[1]))
{
    usage();
}

// Count duplicate characters
$str = $argv[1];
$counts = duplicate_character_counter($str);

// Show all duplicate character counts in order in which they occurred in string (if any)
show_duplicate_character_counts($counts);

```

{% endraw %}

Duplicate Character Counter in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).