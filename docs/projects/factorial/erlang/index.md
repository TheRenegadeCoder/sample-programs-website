---
authors:
- Mark Magahis
- rzuckerm
date: 2019-10-06
featured-image: factorial-in-every-language.jpg
last-modified: 2023-11-21
layout: default
tags:
- erlang
- factorial
title: Factorial in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/erlang/how-to-implement-the-solution.md
- sources/programs/factorial/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(factorial).
-export([main/1]).

usage() ->
    io:format("Usage: please input a non-negative integer~n"),
    halt().

convert_to_integer(Str) ->
    Result = catch string:to_integer(string:strip(Str)),
    case Result of
        {Int, Rest} when Rest == "" ->
            {ok, Int};
        _ ->
            {error, 0}
    end.

main(Args) ->
    if
        length(Args) < 1 ->
            usage();
        true ->
            ok
    end,

    StrValue = lists:nth(1, Args),
    Value = case convert_to_integer(StrValue) of
        {ok, Int} ->
            Int;
        _ ->
            usage()
    end,

    if
        Value < 0 ->
            usage();
        true ->
            ok
    end,

    FValue = factorial(Value),
    io:format("~w~n", [FValue]).

%%--------------------------------------------------------------------
%% Recursively multiply N times N-1 until N <= 1
%%--------------------------------------------------------------------
factorial(0) ->
    1;
factorial(N) ->
    N * factorial(N-1).

```

{% endraw %}

Factorial in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).