If we just want to see it run, we can paste the solution into an
[online Prolog compiler][2] and press Run.

To run it locally, we need a Prolog system. The solution uses SWI-Prolog's
string syntax, so SWI-Prolog is the one to [download][3]; it has installers
for Windows and macOS, and many Linux distributions package it as `swi-prolog`.
With `swipl` on our path and a copy of the solution, we can run it from the
folder that holds it:

```console
swipl hello-world.pl
```

SWI-Prolog loads the file, the `initialization` directive calls `main`, and
`Hello, World!` prints to the console before `halt` ends the program.

[2]: https://onlinecompiler.io/prolog-online-compiler
[3]: https://www.swi-prolog.org/download/stable
