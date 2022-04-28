---

---

# Reverse String in Erlang

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Erlang
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.