---
authors:
- rzuckerm
date: 2025-05-06
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-05-06
layout: default
tags:
- base64-encode-decode
- powershell
title: Base64 Encode Decode in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/powershell/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please provide a mode and a string to encode/decode"
    Exit 1
}

function Get-Base64Encode([string]$Str) {
    $Bytes = [Text.Encoding]::Ascii.GetBytes($Str)
    [Convert]::ToBase64String($Bytes)
}

function Get-Base64Decode([string]$Str) {
    $Bytes = [Convert]::FromBase64String($Str)
    [Text.Encoding]::Ascii.GetString($Bytes)
}

if ($args.Length -lt 2 -or -not $args[1]) {
    Show-Usage
}

$Mode = $args[0]
$Str = $args[1]
switch ($Mode) {
    "encode" {
        $Result = Get-Base64Encode($Str)
    }
    "decode" {
        try {
            $Result = Get-Base64Decode($Str)
        } catch [Management.Automation.MethodInvocationException] {
            Show-Usage
        }
    }
    default {
        Show-Usage 
    }
}

Write-Host $Result

```

{% endraw %}

Base64 Encode Decode in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).