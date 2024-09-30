---
authors:
- rzuckerm
date: 2023-12-11
featured-image: baklava-in-every-language.jpg
last-modified: 2023-12-11
layout: default
tags:
- baklava
- brainfuck
title: Baklava in Brainfuck
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/brainfuck/how-to-implement-the-solution.md
- sources/programs/baklava/brainfuck/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Brainfuck](https://sampleprograms.io/languages/brainfuck) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```brainfuck
; Mem 1 = 7; Mem 2 = 42 (star); Mem 3 = 35; Mem 4 = 7
+++++++         ; Mem 0 = 7
[
    >+          ; Inc Mem 1
    >++++++     ; Add 6 to Mem 2
    >+++++      ; Add 5 to Mem 3
    >+          ; Inc Mem 4
    <<<<-       ; Dec Mem 0
]
; Mem 1 = 10 (newline); Mem 3 = 32 (space); Mem 4 = 11
>+++            ; Add 3 to Mem 1
>>---           ; Sub 3 from Mem 3
>++++           ; Add 4 to Mem 4
[
    ; Dec Mem 4
    -
    ; Display Mem 4 spaces
    ; Mem 5 = Mem 4
    ; Mem 6 = 21 minus 2 * Mem 4
    >>>+++++++  ; Mem 7 = 7
    [
        <+++    ; Add 3 to Mem 6
        >-      ; Dec Mem 7
    ]
    <<<
    [
        <.      ; Display space (Mem 3)
        >>+     ; Inc Mem 5
        >--     ; Sub 2 from Mem 6
        <<-     ; Dec Mem 4
    ]
    ; Display Mem 6 stars
    >>
    [
        <<<<.   ; Display star (Mem 2)
        >>>>-   ; Dec Mem 6
    ]
    ; Display newline (Mem 1)
    <<<<<.
    ; Mem 4 = Mem 5
    >>>>
    [
        <+      ; Inc Mem 4
        >-      ; Dec Mem 5
    ]
    <
]
; Mem 4 = 10
++++++++++
[
    ; Dec Mem 4
    -
    ; Mem 5 = 10 minus Mem 4
    ; Mem 6 = 1 plus 2 * Mem 4
    >++++++++++ ; Mem 5 = 10
    >+          ; Mem 6 = 1
    <<
    [
        >-      ; Dec Mem 5
        >++     ; Add 2 to Mem 6
        <<-     ; Dec Mem 4
    ]
    ; Display Mem 5 spaces
    ; Mem 4 = 10 minus Mem 5
    ++++++++++  ; Mem 4 = 10
    >
    [
        <<.     ; Display Mem 3 (space)
        >-      ; Dec Mem 4
        >-      ; Dec Mem 5
    ]
    ; Display Mem 6 stars
    >
    [
        <<<<.   ; Display Mem 2 (star)
        >>>>-   ; Dec Mem 6
    ]
    ; Display newline (Mem 1)
    <<<<<.
    >>>
]

```

{% endraw %}

Baklava in [Brainfuck](https://sampleprograms.io/languages/brainfuck) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).