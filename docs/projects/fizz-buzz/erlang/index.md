---
authors:
- Caio Ariede
- rzuckerm
date: 2019-10-04
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-11-21
layout: default
tags:
- erlang
- fizz-buzz
title: Fizz Buzz in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/erlang/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(fizz_buzz).
-export([main/1]).

% Run with: escript fizz_buzz.erl

main(_) ->
    fizz_buzz(1, 100).

fizz_buzz(N, Max) when N > Max -> [];
fizz_buzz(N, Max) when N rem 15 == 0 -> io:format("FizzBuzz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) when N rem 5 == 0 -> io:format("Buzz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) when N rem 3 == 0 -> io:format("Fizz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) -> io:format("~p~n", [N]), fizz_buzz(N+1, Max).

```

{% endraw %}

Fizz Buzz in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Caio Ariede
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).