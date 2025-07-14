---
authors:
- rzuckerm
date: 2025-07-14
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2025-07-14
layout: default
tags:
- insertion-sort
- powershell
title: Insertion Sort in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/powershell/how-to-implement-the-solution.md
- sources/programs/insertion-sort/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

# https://en.wikipedia.org/wiki/Insertion_sort#Algorithm
function Invoke-InsertionSort([array]$Values) {
    $n = $Values.Length
    $i = 1
    for ($i = 1; $i -lt $n; $i++) {
        $x = $Values[$i]
        $j = $i
        while ($j -gt 0 -and $Values[$j - 1] -gt $x) {
            $Values[$j] = $Values[$j - 1]
            $j--
        }

        $Values[$j] = $x
    }
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $values = Parse-IntList $args[0]
    if ($values.Length -lt 2) {
        Show-Usage
    }
} catch {
    Show-Usage
}

Invoke-InsertionSort $values
Write-Host ($values -join ', ')

```

{% endraw %}

Insertion Sort in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).