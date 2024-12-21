---
authors:
- rzuckerm
date: 2024-12-21
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-21
layout: default
tags:
- baklava
- prolog
title: Baklava in Prolog
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/prolog/how-to-implement-the-solution.md
- sources/programs/baklava/prolog/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Prolog](https://sampleprograms.io/languages/prolog) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```prolog
:- initialization(main).

baklava(N, NE) :-
    forall(between(N, NE, X), baklava_line(X)).

baklava_line(N) :-
    NSP is abs(N),
    NST is 21 - 2 * NSP,
    output_repeat(" ", NSP),
    output_repeat("*", NST),
    nl.

output_repeat(S, N) :-
    forall(between(1, N, _), write(S)).

main() :-
    baklava(-10, 10),
    halt.

```

{% endraw %}

Baklava in [Prolog](https://sampleprograms.io/languages/prolog) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).