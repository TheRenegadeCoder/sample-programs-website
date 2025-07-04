---
authors:
- rzuckerm
date: 2025-07-04
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2025-07-04
layout: default
tags:
- powershell
- roman-numeral
title: Roman Numeral in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/powershell/how-to-implement-the-solution.md
- sources/programs/roman-numeral/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
$Romans = @{
    M = 1000
    D = 500
    C = 100
    L = 50
    X = 10
    V = 5
    I = 1
}

function Show-Usage() {
    Write-Host 'Usage: please provide a string of roman numerals'
    Exit 1
}

function Show-Error() {
    Write-Host 'Error: invalid string of roman numerals'
    Exit 1
}

function RomanNumeral([string]$Str) {
    $total = 0
    $prevValue = 0
    foreach ($ch in $Str.ToCharArray()) {
        $value = $Romans[[string]$ch]
        if (-not $value) {
            $total = -1
            break
        }

        $total += $value
        if ($prevValue -gt 0 -and $value -gt $prevValue) {
            $total -= 2 * $prevValue
            $prevValue = 0
        } else {
            $prevValue = $value
        }
    }

    $total
}

if ($args.Length -lt 1) {
    Show-Usage
}

$result = RomanNumeral $args[0]
if ($result -lt 0) {
    Show-Error
}

Write-Output $result

```

{% endraw %}

Roman Numeral in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).