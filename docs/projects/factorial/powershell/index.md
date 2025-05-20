---
authors:
- rzuckerm
date: 2025-05-20
featured-image: factorial-in-every-language.jpg
last-modified: 2025-05-20
layout: default
tags:
- factorial
- powershell
title: Factorial in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/powershell/how-to-implement-the-solution.md
- sources/programs/factorial/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input a non-negative integer"
    Exit 1
}

function Get-Factorial([int]$Value) {
    $Product = 1
    if ($Value -gt 0) {
        1..$Value | ForEach-Object { $Product *= $_ }
    }

    $Product
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $Value = [int]::Parse($args[0])
} catch {
    Show-Usage
}

if ($Value -lt 0) {
    Show-Usage
}

Write-Host (Get-Factorial $Value)

```

{% endraw %}

Factorial in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).