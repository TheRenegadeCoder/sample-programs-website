---
title: Baklava in Erlang
layout: default
date: 2019-10-04
featured-image: baklava-in-every-language.jpg
last-modified: 2019-10-04

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(baklava).
-export([start/1]).

-spec start(MaxWidth :: integer()) -> ok.
start(MaxWidth) ->
    baklava(MaxWidth, 0),
    ok.

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

[Baklava](https://sampleprograms.io/projects/baklava) in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Mark Magahis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 04 2019 16:16:30. The solution was first committed on Oct 04 2019 16:00:01. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).