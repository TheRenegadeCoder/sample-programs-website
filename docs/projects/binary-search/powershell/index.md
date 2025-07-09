---
authors:
- rzuckerm
date: 2025-07-07
featured-image: binary-search-in-every-language.jpg
last-modified: 2025-07-07
layout: default
tags:
- binary-search
- powershell
title: Binary Search in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/powershell/how-to-implement-the-solution.md
- sources/programs/binary-search/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

function Test-IsSorted([int[]]$arr) {
    for ($i = 1; $i -lt $arr.Length; $i++) {
        if ($arr[$i - 1] -gt $arr[$i]) {
            return $false
        }
    }

    $true
}

function Invoke-BinarySearch([int[]]$arr, [int]$target) {
    [Array]::BinarySearch($arr, $target)
}

if ($args.Length -lt 2 -or -not $args[0]) {
    Show-Usage
}

try {
    $arr = Parse-IntList $args[0]
    $target = [int]::Parse($args[1])
} catch {
    Show-Usage
}

if (-not (Test-IsSorted $arr)) {
    Show-Usage
}

$idx = Invoke-BinarySearch $arr $target
Write-Output (($idx -ge 0) ? "true" : "false")

```

{% endraw %}

Binary Search in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).