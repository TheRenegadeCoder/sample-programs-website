---
authors:
- rzuckerm
date: 2025-07-14
featured-image: selection-sort-in-every-language.jpg
last-modified: 2025-07-14
layout: default
tags:
- powershell
- selection-sort
title: Selection Sort in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/powershell/how-to-implement-the-solution.md
- sources/programs/selection-sort/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

# Source: https://en.wikipedia.org/wiki/Selection_sort#Implementations
function Invoke-SelectionSort([array]$Values) {
    $n = $Values.Length
    for ($i = 0; $i -lt ($n - 1); $i++) {
        $jMin = $i
        for ($j = $i + 1; $j -lt $n; $j++) {
            if ($Values[$j] -lt $Values[$jMin]) {
                $jMin = $j
            }
        }

        if ($jMin -ne $i) {
            $Values[$i], $Values[$jMin] = $Values[$jMin], $Values[$i]
        }
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

Invoke-SelectionSort $values
Write-Host ($values -join ', ')

```

{% endraw %}

Selection Sort in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).