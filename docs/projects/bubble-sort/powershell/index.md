---
authors:
- rzuckerm
date: 2025-07-14
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2025-07-14
layout: default
tags:
- bubble-sort
- powershell
title: Bubble Sort in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/powershell/how-to-implement-the-solution.md
- sources/programs/bubble-sort/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

# Source: https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort
function Invoke-BubbleSort([array]$Values) {
    $n = $Values.Length
    do {
        $newN = 0
        for ($i = 1; $i -lt $n; $i++) {
            if ($Values[$i - 1] -gt $Values[$i]) {
                $Values[$i - 1], $Values[$i] = $Values[$i], $Values[$i - 1]
                $newN = $i
            }
        }

        $n = $newN
    } while ($n -gt 1)
}

if ($args.Length -lt 1 -or -not $args[0]) {
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

Invoke-BubbleSort $values
Write-Output ($values -join ', ')

```

{% endraw %}

Bubble Sort in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).