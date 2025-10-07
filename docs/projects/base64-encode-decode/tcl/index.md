---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-10-08
layout: default
tags:
- base64-encode-decode
- tcl
title: Base64 Encode Decode in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/tcl/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
#!/usr/bin/env tclsh

proc usage {} {
    puts stderr "Usage: please provide a mode and a string to encode/decode"
    exit 1
}

if {$argc != 2} {
    usage
}

set mode [lindex $argv 0]
set text [lindex $argv 1]

if {$text eq ""} {
    usage
}


switch -- $mode {
    encode {
        set result [binary encode base64 $text]
    }
    decode {
        if {[catch {binary decode base64 $text} result]} {
            usage
        }
	# Tcl’s decoder sometimes tolerates invalid padding, so validate manually
        # Check that input length is a multiple of 4 and only contains valid chars
        if {![regexp {^[A-Za-z0-9+/]*={0,2}$} $text]} {
            usage
        }
        if {[expr {[string length $text] % 4 != 0}]} {
            usage
        }
    }
    default {
        usage
    }
}

puts $result


```

{% endraw %}

Base64 Encode Decode in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).