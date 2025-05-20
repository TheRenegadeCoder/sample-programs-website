---
authors:
- rzuckerm
date: 2025-05-20
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-05-20
layout: default
tags:
- even-odd
- powershell
title: Even Odd in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/powershell/how-to-implement-the-solution.md
- sources/programs/even-odd/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input a number"
    Exit 1
}

function Test-IsEven([int]$Value) {
    $Value % 2 -eq 0
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $Value = [int]::Parse($args[0])
} catch {
    Show-Usage
}

Write-Host ((Test-IsEven $Value) ? "Even" : "Odd")

```

{% endraw %}

Even Odd in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).