---
authors:
- rzuckerm
date: 2025-05-24
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-05-24
layout: default
tags:
- palindromic-number
- powershell
title: Palindromic Number in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/powershell/how-to-implement-the-solution.md
- sources/programs/palindromic-number/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input a non-negative integer"
    Exit 1
}

function Test-IsPalindromicNumber([int]$Value) {
    $Str = [string]$Value
    $Str -eq -join $Str[$Str.Length..0]
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

Write-Host ((Test-IsPalindromicNumber $Value) ? "true" : "false")

```

{% endraw %}

Palindromic Number in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).