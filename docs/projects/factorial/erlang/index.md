---
title: Factorial in Erlang
layout: default
date: 2019-10-06
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-06

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(factorial).
-export([start/1]).

-spec start(Number :: integer()) -> integer().
start(N) 
    when N<0;
         not is_integer(N) ->
    io:format("Usage: please input a non-negative integer~n");
start(0) ->
    factorial(1,1);
start(N) ->
    factorial(N,N).

%%--------------------------------------------------------------------
%% Recursively multiply N times N-1 until N-1=1. Output Accumulator
%%--------------------------------------------------------------------
factorial(1,Acc) ->
    io:format("~w~n", [Acc]);
factorial(N,Acc) ->
    factorial(N-1, (N-1)*Acc).
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).