---
authors:
- rzuckerm
date: 2025-05-24
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-05-24
layout: default
tags:
- longest-word
- powershell
title: Longest Word in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/powershell/how-to-implement-the-solution.md
- sources/programs/longest-word/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string"
    Exit 1
}

function Get-LongestWord([string]$Str) {
    ($Str -split "\s+" | ForEach-Object { $_.Length } | Measure-Object -Maximum).Maximum
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

Write-Host (Get-LongestWord $args[0])

```

{% endraw %}

Longest Word in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).