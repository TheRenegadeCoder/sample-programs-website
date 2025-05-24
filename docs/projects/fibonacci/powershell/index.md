---
authors:
- rzuckerm
date: 2025-05-24
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-05-24
layout: default
tags:
- fibonacci
- powershell
title: Fibonacci in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/powershell/how-to-implement-the-solution.md
- sources/programs/fibonacci/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input the count of fibonacci numbers to output"
    Exit 1
}

function Show-Fibonacci([int]$Value) {
    if ($Value -gt 0) {
        $A, $B = 0, 1
        1..$Value | ForEach-Object {
            $A, $B = $B, ($A + $B)
            Write-Host "${_}: $A"
        }
    }
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

Show-Fibonacci $Value

```

{% endraw %}

Fibonacci in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).