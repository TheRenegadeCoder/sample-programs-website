---
authors:
- rzuckerm
date: 2025-05-10
featured-image: file-input-output-in-every-language.jpg
last-modified: 2025-05-10
layout: default
tags:
- file-input-output
- powershell
title: File Input Output in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/powershell/how-to-implement-the-solution.md
- sources/programs/file-input-output/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Set-File([string]$Filename) {
    try {
        $StreamWriter = [IO.StreamWriter]::new($FileName)
        $StreamWriter.WriteLine("Hello, PowerShell!")
        $StreamWriter.WriteLine("A line here")
        $StreamWriter.WriteLine("A line there")
        $StreamWriter.WriteLine("Goodbye, PowerShell!")
        $true
    } catch {
        Write-Host "Cannot write to file ${Filename}: $($_.Exception.Message)"
        $false
    } finally {
        if ($StreamWriter) {
            $StreamWriter.Close()
            $StreamWriter.Dispose()
        }
    }
}

function Get-File([string]$Filename) {
    try {
        foreach ($Line in Get-Content -Path $Filename -ErrorAction Stop) {
            Write-Host $Line
        }
        $true
    } catch {
        Write-Host "Cannot read from file ${Filename}: $($_.Exception.Message)"
        $false
    }
}

$Filename = "output.txt"
if (-not (Set-File($Filename))) {
    Exit 1
}

if (-not (Get-File($Filename))) {
    Exit 1
}

```

{% endraw %}

File Input Output in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).