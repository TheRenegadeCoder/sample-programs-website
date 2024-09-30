---
authors:
- Mark Magahis
- rzuckerm
date: 2019-10-06
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-11-21
layout: default
tags:
- erlang
- reverse-string
title: Reverse String in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/erlang/how-to-implement-the-solution.md
- sources/programs/reverse-string/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(reverse_string).
-export([main/1]).

%%--------------------------------------------------------------------
%% Reverse a given string
%%--------------------------------------------------------------------
reverse_string(String) ->
   lists:reverse(String).

main(Args) ->
    if
        length(Args) >= 1 ->
            Str = lists:nth(1, Args);
        true ->
            Str = ""
    end,

   ReverseStr = reverse_string(Str),
   io:format("~s~n", [ReverseStr]).

```

{% endraw %}

Reverse String in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).