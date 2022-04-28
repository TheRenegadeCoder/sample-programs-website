---

---

Welcome to the Factorial in Erlang page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Erlang
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.