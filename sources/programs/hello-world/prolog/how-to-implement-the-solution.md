Let's walk through Hello World in Prolog, line by line.

A Prolog file is a set of facts and rules, plus directives that run while the
file loads. The first line is a directive:

```prolog
:- initialization(main).
```

It tells Prolog to call `main` once the whole file has been loaded. Without
it, loading the file would only define `main`, and nothing would print until
someone asked for it at the interactive prompt.

Next comes the rule that does the work. Its head is `main()`, and the body
after `:-` is a list of goals separated by commas, which Prolog runs in order.
The empty brackets are SWI-Prolog syntax for a term with no arguments; in a
rule head, SWI-Prolog treats `main()` the same as plain `main`, so this
defines `main/0`, the predicate the directive calls.

The first goal writes the greeting:

```prolog
write("Hello, World!\n")
```

In SWI-Prolog, text in double quotes is a [string][1], and `write` prints it
as it is, with `\n` ending the line. That detail matters because Prolog
systems disagree here: under the older convention, the same quotes make a
list of character codes, and `write` would print a list of numbers instead of
the greeting.

The last goal, `halt`, ends the program. Otherwise SWI-Prolog would finish
loading the file and then wait at its interactive prompt.

[1]: https://www.swi-prolog.org/pldoc/man?section=strings
