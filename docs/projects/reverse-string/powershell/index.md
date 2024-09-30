---
authors:
- Devin Leaman
- Jeremy Grifski
- rzuckerm
date: 2018-05-28
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- powershell
- reverse-string
title: Reverse String in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/powershell/how-to-implement-the-solution.md
- sources/programs/reverse-string/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
<#
.SYNOPSIS
  A simple script for reversing a String.

.DESCRIPTION
  A simple script for reversing a String in PowerShell in order to show some
features of the language.

.PARAMETER Str
  The string to reverse.

.EXAMPLE
  .\ReverseString.ps1 -Str 'Hello, World'

.EXAMPLE
  .\ReverseString.ps1 "Les Misérables"

.EXAMPLE
  .\ReverseString.ps1 "字樣樣品"

.NOTES
  This script does *not* support emoji as PowerShell only has full support for
emoji within the ISE.
#>
param
(
  [Parameter(Mandatory = $false, Position = 0)]
  [string]$Str
)

$StringBuilder = New-Object -TypeName System.Text.StringBuilder($Str.Length)

for ($x = ($Str.Length - 1); $x -ge 0; $x--) {
  [void]$StringBuilder.Append($Str.Chars($x))
}

Write-Host $StringBuilder.ToString()

```

{% endraw %}

Reverse String in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- Devin Leaman
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).