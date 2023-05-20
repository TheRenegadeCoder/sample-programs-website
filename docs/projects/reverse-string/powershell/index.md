---
title: Reverse String in Powershell
layout: default
date: 2018-05-28
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-05-28

---

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

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- Devin Leaman
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 09:50:39. The solution was first committed on May 28 2018 19:52:57. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).