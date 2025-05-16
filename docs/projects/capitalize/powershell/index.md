---
authors:
- rzuckerm
date: 2025-05-16
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-05-16
layout: default
tags:
- capitalize
- powershell
title: Capitalize in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/powershell/how-to-implement-the-solution.md
- sources/programs/capitalize/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string"
    Exit 1
}

function Get-Capitalize([string]$Str) {
    ([string]$Str[0]).ToUpper() + (-join $Str[1..$Str.Length])
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

Write-Host (Get-Capitalize $args[0])

```

{% endraw %}

Capitalize in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).