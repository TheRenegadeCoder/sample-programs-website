---
authors:
- rzuckerm
date: 2025-07-16
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-07-16
layout: default
tags:
- maximum-array-rotation
- powershell
title: Maximum Array Rotation in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/powershell/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

function Invoke-MaximumArrayRotation([array]$Values) {
    # Calculate sum and initial array rotation
    $s = ($Values | Measure-Object -Sum).Sum
    $w = 0
    for ($i = 0; $i -lt $Values.Length; $i++) {
        $w += $i * $Values[$i]
    }

    # Initialize maximum array rotation
    $wMax = $w

    # Adjust array rotation and update maximum
    $n = $Values.Length
    for ($i = 0; $i -lt ($n - 1); $i++) {
        $w += $n * $Values[$i] - $s
        $wMax = [int][Math]::Max($wMax, $w)
    }

    $wMax
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $values = Parse-IntList $args[0]
} catch {
    Show-Usage
}

$maxValue = Invoke-MaximumArrayRotation $values
Write-Host $maxValue

```

{% endraw %}

Maximum Array Rotation in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).