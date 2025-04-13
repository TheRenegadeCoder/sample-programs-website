---
authors:
- rzuckerm
date: 2025-04-06
featured-image: file-input-output-in-every-language.jpg
last-modified: 2025-04-06
layout: default
tags:
- awk
- file-input-output
title: File Input Output in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/awk/how-to-implement-the-solution.md
- sources/programs/file-input-output/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function write_file(filename) {
    print "Hello from awk" >filename
    print "Line 1" >>filename
    print "Line 2" >>filename
    print "Goodbye from awk" >>filename
    close(filename)
}

# Reference: https://www.gnu.org/software/gawk/manual/html_node/Getline_002fVariable_002fFile.html
function read_file(filename) {
    while (getline line < filename) {
        print line
    }

    close(filename)
}

BEGIN {
    filename = "output.txt"
    write_file(filename)
    read_file(filename)
}

```

{% endraw %}

File Input Output in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).