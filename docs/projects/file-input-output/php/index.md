---
authors:
- Jeremy Grifski
- Juan D Frias
- Parker Johansen
date: 2019-10-14
featured-image: file-input-output-in-every-language.jpg
last-modified: 2022-05-09
layout: default
tags:
- file-input-output
- php
title: File Input Output in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/php/how-to-implement-the-solution.md
- sources/programs/file-input-output/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

function write_file($file_name)
{
    $file = @fopen($file_name, "w");
    if ($file === false) {
        echo "Cannot open file \"", $file_name, "\" for writing.\n";
        return false;
    }

    fwrite($file, "Hello World.\n");
    fwrite($file, "Testing one...\n");
    fwrite($file, "two...\n");
    fwrite($file, "three!\n");

    fflush($file);
    fclose($file);
    return true;
}

function read_file($file_name)
{
    $file = @fopen($file_name, "r");
    if ($file === false) {
        echo "Cannot open file \"", $file_name, "\" for reading.\n";
        return;
    }

    while (!feof($file)) {
        echo fgets($file);
    }

    fclose($file);
}

$file_name = "output.txt";
if (write_file($file_name)) {
    read_file($file_name);
}

```

{% endraw %}

File Input Output in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Juan D Frias
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).