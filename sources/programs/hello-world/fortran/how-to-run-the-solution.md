If we just want to see it run, we can paste the solution into an
[online Fortran compiler][1] and press Run.

To run it locally, we need a Fortran compiler. The free option is gfortran,
which is part of GCC, and the Fortran community keeps
[install instructions for Windows, macOS and Linux][2]. With gfortran on our
path and a copy of the solution, we can compile and run it from the folder
that holds it:

```console
gfortran -o hello-world hello-world.f95
./hello-world
```

On Windows, the second command is `hello-world.exe`. The `.f95` extension
tells gfortran the source uses the free-form layout of Fortran 90 and later,
so no special flags are needed. When the program runs, `Hello, World!` prints
to the console.

[1]: https://onlinecompiler.io/fortran-online-compiler
[2]: https://fortran-lang.org/learn/os_setup/install_gfortran/
