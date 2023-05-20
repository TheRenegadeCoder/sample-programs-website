---
title: Bubble Sort in Erlang
layout: default
date: 2019-10-03
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-03

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(bubble_sort).
-export([start/0, start/1]).

%% Compile with:   erlc bubble_sort.erl
%% Run with:       erl -noshell -run bubble_sort start <INPUT> -s init stop

start() ->
    io:format("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"~n").
start([""]) ->
    io:format("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"~n");
start([InputString]) ->
    case handle_input(InputString) of
        invalid_input ->
            io:format("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"~n");
        NumList ->
            Result = bubble_sort(NumList),
            handle_output(Result)
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


handle_input(InputString) ->    
    case binary:split(list_to_binary([C || C <- InputString, C =/= $ ]), <<",">>, [global, trim_all]) of 
        [] ->
            invalid_input;
        [_] ->
            invalid_input;
        BinaryNums ->
            [binary_to_integer(Bin) || Bin <- BinaryNums]
    end.


handle_output([Num]) ->
    io:format("~p~n", [Num]);
handle_output([Num|NumList]) ->
    io:format("~p, ", [Num]),
    handle_output(NumList).
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Jacky Hui

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).