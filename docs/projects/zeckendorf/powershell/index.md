---
authors:
- rzuckerm
date: 2026-03-07
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-03-07
layout: default
tags:
- powershell
- zeckendorf
title: Zeckendorf in PowerShell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/powershell/how-to-implement-the-solution.md
- sources/programs/zeckendorf/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [PowerShell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input a non-negative integer"
    Exit 1
}

function Get-Fibonacci-Values([int]$Value) {
    $a = 1
    $b = 2
    while ($a -le $Value) {
        $a
        $a, $b = $b, ($a + $b)
    }
}

function Get-Zeckendorf-Values([int]$Value) {
    $fibs = Get-Fibonacci-Values($Value)
    $n = $fibs.Length - 1
    while ($n -ge 0 -and $Value -gt 0) {
        $f = $fibs[$n]
        if ($Value -ge $f) {
            $f
            $Value -= $f
            $n -= 2
        } else {
            $n--
        }
    }
}

if ($args.Length -lt 1) {
    Show-Usage
}

try {
    $value = [int]::Parse($args[0])
} catch {
    Show-Usage
}

if ($value -lt 0) {
    Show-Usage
}

$values = Get-Zeckendorf-Values($value)
Write-Host ($values -join ', ')

```

{% endraw %}

Zeckendorf in [PowerShell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).