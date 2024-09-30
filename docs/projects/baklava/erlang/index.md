---
authors:
- Mark Magahis
- rzuckerm
date: 2019-10-04
featured-image: baklava-in-every-language.jpg
last-modified: 2023-11-21
layout: default
tags:
- baklava
- erlang
title: Baklava in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/erlang/how-to-implement-the-solution.md
- sources/programs/baklava/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(baklava).
-export([main/1]).

-spec baklava(MaxWidth :: integer(),
              Incrementor :: integer()) -> ok.
%%--------------------------------------------------------------------
%% Recursively prints the top half of the baklava 
%%--------------------------------------------------------------------
baklava(MaxWidth, MaxWidth) ->
    print((MaxWidth*2)+1, star),
    reverse_baklava(MaxWidth, MaxWidth-1);
baklava(MaxWidth, Incrementor) ->
    print(MaxWidth-Incrementor, space),
    print((Incrementor*2)+1, star),
    baklava(MaxWidth, Incrementor+1).

-spec reverse_baklava(MaxWidth :: integer(),
                      Decrementor :: integer()) -> ok.
%%--------------------------------------------------------------------
%% Recursively prints the bottom half of the baklava
%%--------------------------------------------------------------------
reverse_baklava(MaxWidth, 0) ->
    print(MaxWidth, space),
    print(1, star);
reverse_baklava(MaxWidth, Decrementor) ->
    print(MaxWidth-Decrementor, space),
    print((Decrementor*2)+1, star),
    reverse_baklava(MaxWidth, Decrementor-1).

-spec print(Number :: integer(),
            Type :: star | space) -> ok.
%%--------------------------------------------------------------------
%% Recursively prints the specified Number of stars or spaces
%%--------------------------------------------------------------------
main(_) ->
    baklava(10, 0).

print(0,star) ->
    io:format("~n");
print(0,_) ->
    ok;
print(N, space) ->
    io:format(" "),
    print(N-1, space);
print(N, star) ->
    io:format("*"),
    print(N-1, star).

```

{% endraw %}

Baklava in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).