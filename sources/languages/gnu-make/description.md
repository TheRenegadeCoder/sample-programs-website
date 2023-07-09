According to [Wikipedia][1], `make` is an automated tool for building software.
It was created in 1976 by [Stuart Freedman][2] for [Unix][3] systems, and it is
still used today on Unix and Unix-like systems (such as [Linux][4] and
[MacOS][5]). For such systems, [GNU make][6] is the most prevelant.

In general, make gets it instructions on what to build based on a Makefile.
The syntax for a Makefile is like this:

```make
target1 [target2 ...]: dependency1 [dependency2 ...]
    command1
    command2
    ...
```

The "target" is what is being built, "dependencies" are what the target
depends upon, and "commands" are what is executed when the target is built.
It should be noted `make` is a whitespace-sensitive language. Before each
command, is a tab character. It you try to use spaces, you'll get this error:

```
*** missing separator.  Stop.
```

The way `make` works is that a target will be built if it does not exist
or it is older that its dependencies.

Here's an example of file called `Makefile` (which is the default filename
that `make` looks for):

```make
hello: hello.c
    cc hello.c -o hello
```

It build a single C program called `hello.c` into a executable called `hello`.
The command perform this build is this:

```bash
make hello
```

If `hello` does not exist, or if `hello.c` was modified after `hello` was
built, the `cc` command is executed the builds the code. If the `make` command
is run again, it will indicate `'hello' is up to date`.

In addition to being a build system, GNU make also has a number of other
useful features:

* [Variables][7] that can be used for everything from simple assignment
  to defining user-defined functions in the form of macros.
* [Built-in functions][8] for manipulating text.
* [Conditionals][9] that can be used to ignore or include certain portions
  of a Makefile.

Although GNU make is not really intended as a programming language, these
features allow it to behave as if it were. It can even similate control
flow with certain built-in functions like these:

* [foreach][10]
* [if][11]
* [call][12]

Loops can be simulated using macros that invoke themselves recursively.

[1]: https://en.wikipedia.org/wiki/Make_(software)
[2]: https://en.wikipedia.org/wiki/Stuart_Feldman
[3]: https://en.wikipedia.org/wiki/Unix
[4]: https://en.wikipedia.org/wiki/Linux
[5]: https://en.wikipedia.org/wiki/MacOS
[6]: https://www.gnu.org/software/make/
[7]: https://www.gnu.org/software/make/manual/html_node/Using-Variables.html
[8]: https://www.gnu.org/software/make/manual/html_node/Functions.html
[9]: https://www.gnu.org/software/make/manual/html_node/Conditionals.html
[10]: https://www.gnu.org/software/make/manual/html_node/Foreach-Function.html
[11]: https://www.gnu.org/software/make/manual/html_node/Conditional-Functions.html#index-if-1
[12]: https://www.gnu.org/software/make/manual/html_node/Call-Function.html
