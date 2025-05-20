---
authors:
- rzuckerm
date: 2025-05-20
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-05-20
layout: default
tags:
- powershell
- prime-number
title: Prime Number in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/powershell/how-to-implement-the-solution.md
- sources/programs/prime-number/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input a non-negative integer"
    Exit 1
}

function Test-IsPrime([int]$Value) {
    if ($Value -lt 2 -or ($Value -ne 2 -and $Value % 2 -eq 0)) {
        return $false
    }

    $Q = [Math]::Floor([Math]::Sqrt($Value))
    for ($X = 3; $X -le $Q; $X += 2) {
        if ($Value % $X -eq 0) {
            return $false
        }
    }

    $true
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

Write-Host ((Test-IsPrime $Value) ? "prime" : "composite")

```

{% endraw %}

Prime Number in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).