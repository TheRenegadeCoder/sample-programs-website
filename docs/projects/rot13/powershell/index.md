---
authors:
- rzuckerm
date: 2025-05-11
featured-image: rot13-in-every-language.jpg
last-modified: 2025-05-11
layout: default
tags:
- powershell
- rot13
title: Rot13 in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/powershell/how-to-implement-the-solution.md
- sources/programs/rot13/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string to encrypt"
    Exit 1
}

function Get-Rot13([string]$Str) {
    # -regex is case-insensitve
    $Result = switch -regex ($Str.ToCharArray()) {
        "[a-m]" { [char]([byte]$_ + 13) } # A-M, a-m -> N-Z, n-z
        "[n-z]" { [char]([byte]$_ - 13) } # N-Z, n-z -> A-M, a-m
        default { $_ } # Else, don't change
    }
    -join $Result
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

Write-Host (Get-Rot13($args[0]))

```

{% endraw %}

Rot13 in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).