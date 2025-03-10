---
authors:
- rzuckerm
date: 2023-12-21
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-12-21
layout: default
tags:
- brainfuck
- capitalize
title: Capitalize in Brainfuck
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/brainfuck/how-to-implement-the-solution.md
- sources/programs/capitalize/brainfuck/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Brainfuck](https://sampleprograms.io/languages/brainfuck) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```brainfuck
[
    Source for division algorithm:
    https://stackoverflow.com/questions/27905818/divmod-algorithm-in-brainfuck

    Source for error message text:
    https://copy.sh/brainfuck/text.html
]
; Mem 0 = 1 (indicate first char)
+
; Mem 1 = input char; loop while not null
>,[
    ; Copy input char to Mem 2 and 3; setting Mem 1 to 0
    >[-]
    >[-]
    <<[>+>+<<-]
    ; If first char;
    <[
        ; Mem 5 = 26; Mem 3 = input char minus 97 ('a'); Mem 4 = 0 (uninitialized)
        >>>>>>++++++++++[   ; Mem 6 = 10
            <+++            ; Add 3 to Mem 5
            <<----------    ; Sub 10 from Mem 3
            >>>-            ; Dec Mem 6
        ]
        <----               ; Sub 4 from Mem 5
        <<+++               ; Add 3 to Mem 3
        ; Mem 3 = junk; Mem 4 = n; Mem 5 = d minus r; Mem 6 = r; Mem 7 = q
        ; where:
        ; * n = input char minus 97 (numerator)
        ; * d = 26 (denominator)
        ; * r = n % d (remainder)
        ; * q = n / d (quotient)
        ;
        ; q will be zero if input char is lowercase; not zero otherwise
        [->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]
        ; Sub 32 from Mem 2 (copy of input char) to potentially make it uppercase
        <<++++[             ; Mem 1 = 4
            >--------       ; Sub 8 from Mem 2
            <-              ; Dec Mem 1
        ]
        ; If Mem 7 (q) is not zero (not a lowercase char); add 32 to Mem 2 to undo above
        ; (restore copy of input char)
        >>>>>>[
            <<<<<<++++[     ; Mem 1 = 4
                >++++++++   ; Add 8 to Mem 2
                <-          ; Dec Mem 1
            ]
            >>>>>>[-]       ; Mem 7 = 0
        ]
        ; Mem 0 = 0 (indicate not first char)
        <<<<<<<[-]
    ]
    ; Output Mem 32 (copy of input char; uppercased for first char)
    >>.
    ; Mem 1 = input char
    <,
]
; If first char was null; display error message
<[
    [-]
    -[--->+<]>.
    +[--->+<]>+.
    ++[->+++<]>++.
    ++++++.
    --.
    +++[->+++<]>++.
    [-->+<]>+++.
    [-->+++++++<]>.
    ----.
    -------.
    ----.
    --[--->+<]>--.
    ++++[->+++<]>.
    --[--->+<]>-.
    [-->+++++++<]>.
    ++.
    ---.
    +++++++.
    [------>+<]>.
    -----.
    +.
    --[--->+<]>-.
    [->+++<]>+.
    -[->+++<]>.
    ---[->++++<]>-.
    +.
    --.
    ---------.
    +++++.
    -------.
    <
]

```

{% endraw %}

Capitalize in [Brainfuck](https://sampleprograms.io/languages/brainfuck) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).