---
authors:
- rzuckerm
date: 2025-07-20
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-07-20
layout: default
tags:
- powershell
- transpose-matrix
title: Transpose Matrix in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/powershell/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please enter the dimension of the matrix and the serialized matrix"
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

function ConvertTo-Matrix([int]$numCols, [int]$numRows, [array]$values) {
    @(0..($numRows - 1) | ForEach-Object { , $values[($_ * $numCols)..($_ * $numCols + $numCols - 1)]})
}

function Invoke-TransposeMatrix($matrix) {
    @(0..($matrix[0].Length - 1) | ForEach-Object {
        $i = $_
        , (0..($matrix.Length - 1) | ForEach-Object { $matrix[$_][$i]})
    })
}

function ConvertFrom-Matrix([int[][]]$matrix) {
    @($matrix | ForEach-Object { $_ })
}

if ($args.Length -lt 3 -or -not $args[2]) {
    Show-Usage
}

try {
    $numCols = [int]::Parse($args[0])
    $numRows = [int]::Parse($args[1])
    $values = Parse-IntList($args[2])
    if ($numCols * $numRows -ne $values.Length) {
        Show-Usage
    }
} catch {
    Show-Usage
}

$matrix = ConvertTo-Matrix $numCols $numRows $values
$tMatrix = Invoke-TransposeMatrix $matrix
$tValues = ConvertFrom-Matrix $tMatrix
Write-Output ($tValues -join ', ')

```

{% endraw %}

Transpose Matrix in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).