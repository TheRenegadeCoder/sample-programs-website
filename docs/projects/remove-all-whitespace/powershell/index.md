---
authors:
- rzuckerm
date: 2025-07-04
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-07-04
layout: default
tags:
- powershell
- remove-all-whitespace
title: Remove All Whitespace in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/powershell/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string"
    Exit 1
}

function Invoke-RemoveAllWhitespace([string]$Str) {
    $Str -replace "\s", ""
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

Write-Output (Invoke-RemoveAllWhitespace $args[0])

```

{% endraw %}

Remove All Whitespace in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).