---
title: Reverse String in Erlang
layout: default
date: 2019-10-06
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-10-06

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(reverse_string).
-export([start/1]).

-spec start(StringOrAtom :: list() | atom() | integer()) -> 
   list() | atom() | integer().
%%--------------------------------------------------------------------
%% Reverse a given string, atom, or integer
%%--------------------------------------------------------------------
start(String) when is_list(String)  ->
   lists:reverse(String);

start(Atom) when is_atom(Atom) ->
   list_to_atom(lists:reverse(atom_to_list(Atom)));

start(Number) when is_integer(Number) ->
   list_to_integer(lists:reverse(integer_to_list(Number))).
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).