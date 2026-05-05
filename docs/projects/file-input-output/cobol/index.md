---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-05
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- cobol
- file-input-output
title: File Input Output in COBOL
title1: File Input
title2: Output in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/cobol/how-to-implement-the-solution.md
- sources/programs/file-input-output/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. file-input-output.

environment division.
input-output section.
file-control.
    select output-file assign to "output.txt"
        organization is line sequential
        file status is ws-status.

data division.
file section.
fd output-file.
01 file-line pic x(256).

working-storage section.
01 ws-status        pic xx.
   88 file-ok       value "00".
   88 file-eof      value "10".

01 ws-message       pic x(256) value "Hello from COBOL!".
01 ws-eof-flag      pic x value "n".
   88 eof           value "y".
   88 not-eof       value "n".

procedure division.
main.
    perform write-file
    perform read-file
    stop run.

write-file.
    open output output-file

    if not file-ok
        display "Error: could not open file for writing"
        stop run
    end-if

    move ws-message to file-line
    write file-line

    close output-file.

read-file.
    open input output-file

    if not file-ok
        display "Error: could not open file for reading"
        stop run
    end-if

    set not-eof to true
    perform until eof
        read output-file
            at end
                set eof to true
            not at end
                display function trim(file-line)
        end-read
    end-perform

    close output-file.
```

{% endraw %}

File Input Output in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).