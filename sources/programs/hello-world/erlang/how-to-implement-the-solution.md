Erlang looks scary when you first look at it, so we'll show the full program and
then we'll break it down into parts to fully describe it.

### Breaking it down

The first key part of an Erlang program is the `-module().` preprocessor directive:

```erlang
-module(hello_world).
```

Every Erlang file **must** start with this directive or you'll get a compiler error like the following:

```
file.erl:2: no module definition
```

Next, to use functions from the module we've written we have to export them explicitly.

```erlang
-export([main/1]).
```

This exports our `main` function, it takes one argument so we reference the function as `main/1`. The number of arguments is called the "arity" of the function.


Functions in Erlang start with an atom (for now, think of these as just lowercase letters + underscores), then the parameters, followed by an arrow `->`. The following functions are both valid:

```erlang
my_function() ->
  ok.

myfunction() ->
  ok.
```

Our `main` function only does one thing for this simple program, it calls the `format` function from the `io` module to print characters to standard output by default. `io:format()`. The string `"Hello world!~n"` includes the newline control sequence `~n` - you can see a list of control sequences available for use in the documentation for `io:fwrite` [here][1] (scroll down to "Available control sequences").

[1]: https://www.erlang.org/doc/man/io.html#fwrite-1
