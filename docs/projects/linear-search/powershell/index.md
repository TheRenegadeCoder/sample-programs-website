---
authors:
- rzuckerm
date: 2025-07-09
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-07-09
layout: default
tags:
- linear-search
- powershell
title: Linear Search in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/powershell/how-to-implement-the-solution.md
- sources/programs/linear-search/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

function Invoke-LinearSearch([int[]]$arr, [int]$target) {
    $arr.IndexOf($target)
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

$idx = Invoke-LinearSearch $arr $target
Write-Output (($idx -ge 0) ? "true" : "false")

```

{% endraw %}

Linear Search in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).