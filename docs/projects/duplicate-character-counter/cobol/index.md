---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-30
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- cobol
- duplicate-character-counter
title: Duplicate Character Counter in COBOL
title1: Duplicate Character
title2: Counter in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/cobol/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. duplicate-character-counter.

data division.
working-storage section.

01 input-str        pic x(200).
01 usage-msg        pic x(50) value 'Usage: please provide a string'.

01 i                pic 9(4).
01 len              pic 9(4).

01 ascii-table.
   05 ascii-map occurs 256 times pic 9(4) value 0.

01 seen-table.
   05 seen occurs 256 times pic 9 value 0.

01 current-char     pic x.
01 ascii-val        pic 9(4).

01 has-duplicates   pic 9 value 0.

01 out-count        pic z(4)9.

procedure division.

main.

    accept input-str from argument-value

    if input-str = spaces
        display usage-msg
        stop run
    end-if

    move function length(function trim(input-str)) to len

    if len = 0
        display usage-msg
        stop run
    end-if

    perform varying i from 1 by 1 until i > len
        move input-str(i:1) to current-char
        move function ord(current-char) to ascii-val
        add 1 to ascii-map(ascii-val)
    end-perform

    perform varying i from 1 by 1 until i > len

        move input-str(i:1) to current-char
        move function ord(current-char) to ascii-val

        if ascii-map(ascii-val) > 1 and seen(ascii-val) = 0

            move ascii-map(ascii-val) to out-count

            display current-char ": " function trim(out-count)

            move 1 to seen(ascii-val)
            move 1 to has-duplicates
        end-if

    end-perform

    if has-duplicates = 0
        display "No duplicate characters"
    end-if

    stop run.
```

{% endraw %}

Duplicate Character Counter in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).