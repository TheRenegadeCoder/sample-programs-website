---
authors:
- rzuckerm
date: 2025-07-16
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-07-16
layout: default
tags:
- maximum-subarray
- powershell
title: Maximum Subarray in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/powershell/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

# Find maximum subarray using Kadane's algorithm.
# Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted
function Invoke-MaximumSubarray([array]$Values) {
    $bestSum = [int]::MinValue
    $currentSum = 0
    foreach ($value in $Values) {
        $currentSum = $value + [int][Math]::Max(0, $currentSum)
        $bestSum = [int][Math]::Max($bestSum, $currentSum)
    }

    $bestSum
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $values = Parse-IntList $args[0]
} catch {
    Show-Usage
}

$maxValue = Invoke-MaximumSubarray $values
Write-Host $maxValue

```

{% endraw %}

Maximum Subarray in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).