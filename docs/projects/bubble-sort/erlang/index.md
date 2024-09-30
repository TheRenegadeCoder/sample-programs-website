---
authors:
- Jacky Hui
- rzuckerm
date: 2019-10-03
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2023-11-21
layout: default
tags:
- bubble-sort
- erlang
title: Bubble Sort in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/erlang/how-to-implement-the-solution.md
- sources/programs/bubble-sort/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(bubble_sort).
-export([main/1]).

%% Run with: escript bubble_sort.erl <INPUT>

usage() ->
    io:format("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"~n"),
    halt().

convert_list_to_integers(Str) ->
    Values = string:tokens(Str, ","),
    NumCommas = count_commas(Str),
    NumValues = length(Values),
    if
        (NumCommas + 1) == NumValues ->
            convert_values(Values);
        true ->
            {error, []}
    end.

count_commas([]) ->
    0;
count_commas([$, | Rest]) ->
    1 + count_commas(Rest);
count_commas([_ | Rest]) ->
    count_commas(Rest).

convert_values([]) ->
    {ok, []};
convert_values([ValueStr | Rest]) ->
    case convert_to_integer(ValueStr) of
        {ok, Value} ->
            case convert_values(Rest) of
                {ok, RestValues} ->
                    {ok, [Value | RestValues]};
                _ ->
                    {error, []}
            end;
        _ ->
            {error, []}
    end.

convert_to_integer(Str) ->
    Result = catch string:to_integer(string:strip(Str)),
    case Result of
        {Int, Rest} when Rest == "" ->
            {ok, Int};
        _ ->
            {error, 0}
    end.

bubble_sort(List) -> bubble_sort(List, [], false).

bubble_sort([A, B | T], Acc, _) when A > B ->
    bubble_sort([A | T], [B | Acc], true);
bubble_sort([A, B | T], Acc, Tainted) ->
    bubble_sort([B | T], [A | Acc], Tainted);
bubble_sort([A | T], Acc, Tainted) ->
    bubble_sort(T, [A | Acc], Tainted);
bubble_sort([], Acc, true) ->
    bubble_sort(lists:reverse(Acc));
bubble_sort([], Acc, false) ->
    lists:reverse(Acc).


handle_output([Num]) ->
    io:format("~p~n", [Num]);
handle_output([Num|NumList]) ->
    io:format("~p, ", [Num]),
    handle_output(NumList).

main(Args) ->
    if
        length(Args) < 1 ->
            usage();
        true ->
            ok
    end,

    StrValue = lists:nth(1, Args),
    Values = case convert_list_to_integers(StrValue) of
        {ok, Result} ->
            Result;
        _ ->
            usage()
    end,

    if
        length(Values) < 2 ->
            usage();
        true ->
            ok
    end,

    SortedValues = bubble_sort(Values),
    handle_output(SortedValues).

```

{% endraw %}

Bubble Sort in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Jacky Hui
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).