---

title: Fizz Buzz in Erlang
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Fizz Buzz in Erlang page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```erlang
-module(fizz_buzz).
-export([start/0]).

% Run with: erl -noshell -run fizz_buzz -s init stop

start() ->
    fizz_buzz(1, 100).

fizz_buzz(N, Max) when N > Max -> [];
fizz_buzz(N, Max) when N rem 15 == 0 -> io:format("FizzBuzz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) when N rem 5 == 0 -> io:format("Buzz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) when N rem 3 == 0 -> io:format("Fizz~n", []), fizz_buzz(N+1, Max);
fizz_buzz(N, Max) -> io:format("~p~n", [N]), fizz_buzz(N+1, Max).
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).