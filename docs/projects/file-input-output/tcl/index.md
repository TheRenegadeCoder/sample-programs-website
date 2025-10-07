---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-08
featured-image: file-input-output-in-every-language.jpg
last-modified: 2025-10-08
layout: default
tags:
- file-input-output
- tcl
title: File Input Output in Tcl
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/tcl/how-to-implement-the-solution.md
- sources/programs/file-input-output/tcl/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Tcl](https://sampleprograms.io/languages/tcl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tcl
#!/usr/bin/env tclsh

proc writeToFile {filename} {
    if {[catch {set fh [open $filename w]} err]} {
        puts "Error opening file for writing \"$filename\": $err"
        return 1
    }

    if {[catch {
        puts $fh "A line of text"
        puts $fh "Another line of text"
        flush $fh
    } err]} {
        puts "Error writing to file \"$filename\": $err"
        close $fh
        return 1
    }

    close $fh
    return 0
}

proc readFromFile {filename} {
    if {[catch {set fh [open $filename r]} err]} {
        puts "Error reading from file \"$filename\": $err"
        return 1
    }

    set linesRead 0
    if {[catch {
        while {[gets $fh line] >= 0} {
            puts $line
            incr linesRead
        }
    } err]} {
        puts "Error reading from file \"$filename\": $err"
        close $fh
        return 1
    }

    if {$linesRead == 0} {
        puts "(File \"$filename\" is empty)"
    }

    close $fh
    return 0
}

set filename "output.txt"
if {[ writeToFile $filename] != 0} { exit 1 }
if {[readFromFile $filename] != 0} { exit 1 }

exit 0


```

{% endraw %}

File Input Output in [Tcl](https://sampleprograms.io/languages/tcl) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).