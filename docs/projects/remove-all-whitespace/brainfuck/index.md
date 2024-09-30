---
authors:
- rzuckerm
date: 2023-12-21
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-12-21
layout: default
tags:
- brainfuck
- remove-all-whitespace
title: Remove All Whitespace in Brainfuck
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/brainfuck/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/brainfuck/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Brainfuck](https://sampleprograms.io/languages/brainfuck) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```brainfuck
[
    Source for error message text:
    https://copy.sh/brainfuck/text.html
]
; Mem 0 = 1 (indicate no input)
+
; Mem 1 = input; Loop while input not null
>,[
    ; Mem 0 = 0 (indicate input)
    <[-]
    ; Mem 2 = input; Mem 3 = input; Mem 1 = 0
    >>[-]                       ; Mem 2 = 0
    >[-]                        ; Mem 3 = 0
    <<[
        >+                      ; Inc Mem 2
        >+                      ; Mem Mem 3
        <<-                     ; Dec Mem 1
    ]
    ; Sub 9 from Mem 3; If not zero (not tab)
    >>---------[
        ; Dec Mem 3; If not zero (not newline)
        -[
            ; Sub 3 from Mem 3; If not zero (not carriage return)
            ---[
                ; Sub 19 from Mem 3; If not zero (not space)
                >+++[           ; Mem 4 = 3
                    <------     ; Sub 6 from Mem 3
                    >-          ; Dec Mem 4
                ]
                <-              ; Dec Mem 3
                [
                    ; Display input (Mem 2) and reset Mem 3
                    <.
                    >[-]
                ]
            ]
        ]
    ]
    ; Mem 1 = input
    <<,
]
; If no input; display error message
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
    [-]
]

```

{% endraw %}

Remove All Whitespace in [Brainfuck](https://sampleprograms.io/languages/brainfuck) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).