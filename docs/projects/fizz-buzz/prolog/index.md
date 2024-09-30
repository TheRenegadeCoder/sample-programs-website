---
authors:
- sabrinahuwang
date: 2023-06-10
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-06-10
layout: default
tags:
- fizz-buzz
- prolog
title: Fizz Buzz in Prolog
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/prolog/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/prolog/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Prolog](https://sampleprograms.io/languages/prolog) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```prolog
% Portions of this solution were derived through the assistance of ChatGPT.
:- initialization(main).

fizzbuzz(N) :-
    fizzbuzz_helper(1, N).

fizzbuzz_helper(X, N) :-
    X > N, !.
fizzbuzz_helper(X, N) :-
    (X mod 15 =:= 0 ->
        write('FizzBuzz'), nl
    ; X mod 3 =:= 0 ->
        write('Fizz'), nl
    ; X mod 5 =:= 0 ->
        write('Buzz'), nl
    ;
        write(X), nl
    ),
    X1 is X + 1,
    fizzbuzz_helper(X1, N).

main() :-
    fizzbuzz(100),
    halt.
```

{% endraw %}

Fizz Buzz in [Prolog](https://sampleprograms.io/languages/prolog) was written by:

- sabrinahuwang

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).