---
authors:
- rzuckerm
date: 2025-05-20
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-05-20
layout: default
tags:
- duplicate-character-counter
- powershell
title: Duplicate Character Counter in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/powershell/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string"
    Exit 1
}

function Get-DuplicateCharacterCounter([string]$Str) {
    $Counts = @{}
    $Str.ToCharArray() | ForEach-Object { $Counts[$_] += 1 }
    $Counts
}

function Show-DuplicateCharacterCounter([string]$Str, [object]$Counts) {
    $Dupes = $false
    $Str.ToCharArray() | Select-Object -Unique | ForEach-Object {
        if ($Counts[$_] -gt 1) {
            Write-Host "${_}: $($Counts[$_])"
            $Dupes = $true
        }
    }

    if (-not $Dupes) {
        Write-Host "No duplicate characters"
    }
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

$Str = $args[0]
$Counts = Get-DuplicateCharacterCounter $Str
Show-DuplicateCharacterCounter $Str $Counts

```

{% endraw %}

Duplicate Character Counter in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).