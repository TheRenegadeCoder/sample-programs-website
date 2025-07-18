---
authors:
- rzuckerm
date: 2025-07-16
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-07-16
layout: default
tags:
- longest-palindromic-substring
- powershell
title: Longest Palindromic Substring in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/powershell/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a string that contains at least one palindrome"
    Exit 1
}

# Source: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
function Invoke-LongestPalindromicSubstring($Str) {
    $lcStr = $Str.ToLower()

    # Initialize array indicating where match between two strings
    $n = $Str.Length
    $matches =  @(1..$n | ForEach-Object { , (@($false) * $n) })

    # Indicate all length 1 strings match
    for ($i = 0; $i -lt $n; $i++) {
        $matches[$i][$i] = $true
    }

    # Find all length 2 matches
    $start = 0
    $maxLen = 1
    for ($i = 0; $i -lt $n - 1; $i++) {
        if ($lcStr[$i] -eq $lcStr[$i + 1]) {
            $matches[$i][$i + 1] = $true
            if ($maxLen -lt 2) {
                $start = $i
                $maxLen = 2
            }
        }
    }

    # Find all length 3 or higher matches
    for ($len = 3; $len -le $n; $len++) {
        # Loop through each starting character
        for ($i = 0; $i -lt $n - $len + 1; $i++) {
            # If match for one character in from start and end characters
            # and start and end characters match, set match for start and
            # end characters, and update max length
            $j = $i + $len - 1
            if ($matches[$i + 1][$j - 1] -and $lcStr[$i] -eq $lcStr[$j]) {
                $matches[$i][$j] = $true
                if ($len -gt $maxLen) {
                    $start = $i
                    $maxLen = $len
                }
            }
        }
    }

    $Str.Substring($start, $maxLen)
}

if ($args.Length -lt 1 -or -not $args[0]) {
    Show-Usage
}

$result = Invoke-LongestPalindromicSubstring $args[0]
if ($result.Length -lt 2) {
    Show-Usage
}

Write-Output $result

```

{% endraw %}

Longest Palindromic Substring in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).