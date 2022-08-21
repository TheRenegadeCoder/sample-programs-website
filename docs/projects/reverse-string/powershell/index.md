---

title: Reverse String in Powershell
layout: default
date: 2022-04-28
last-modified: 2022-08-21

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
﻿<#
.SYNOPSIS
  A simple script for reversing a String.

.DESCRIPTION
  A simple script for reversing a String in PowerShell in order to show some
features of the language.

.PARAMETER Input
  The string to reverse.

.EXAMPLE
  .\Reverse-String.ps1 -Input 'Hello, World'

.EXAMPLE
  .\Reverse-String.ps1 "Les Misérables"

.EXAMPLE
  .\Reverse-String.ps1 "字樣樣品"

.NOTES
  This script does *not* support emoji as PowerShell only has full support for
emoji within the ISE.
#>
param
(
  [Parameter(Mandatory = $true,
             Position = 0)]
  [ValidateNotNullOrEmpty()]
  [string]$Input
)

$StringBuilder = New-Object -TypeName System.Text.StringBuilder($Input.Length)

for ($x = ($Input.Length - 1); $x -ge 0; $x--) {
  [void]$StringBuilder.Append($Input.Chars($x))
}

Write-Host $StringBuilder.ToString()
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- Devin Leaman

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).