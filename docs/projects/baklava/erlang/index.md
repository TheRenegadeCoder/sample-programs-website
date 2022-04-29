---

title: Baklava in Erlang
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Erlang page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Erlang
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.