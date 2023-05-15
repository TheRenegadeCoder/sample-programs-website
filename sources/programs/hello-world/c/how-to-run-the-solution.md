Now, if we want to run the solution, we'll need to [get a hold of a C compiler][1].
In addition, we'll probably want to [get a copy of Hello World in C][2]. With both
prerequisites out of the way, all we have to do is navigate to our file and run
the following commands from the command line:

```console
gcc -o hello-world hello-world.c
./hello-world
```

Of course, these are Unix/Linux instructions. If we're on Windows, it may be easier
to take advantage of an [online C compiler][3]. Alternatively, we can leverage a tool
like [MinGW][4].

[1]: https://gcc.gnu.org/
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/c/c/hello-world.c
[3]: https://www.programiz.com/c-programming/online-compiler/
[4]: https://www.mingw-w64.org/
