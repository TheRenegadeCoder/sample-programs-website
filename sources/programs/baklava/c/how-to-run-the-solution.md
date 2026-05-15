If we want to compile and run the program on a computer, we first need a C
compiler installed. Common choices include GCC, Clang, and Microsoft Visual
C++ (MSVC).

Once a compiler is available, we can open a terminal in the same directory as
the source file and compile the program.

For example, using GCC:
```sh
gcc -o baklava baklava.c
./baklava
```
or using Clang:
```sh
clang -o baklava baklava.c
./baklava
```
On Windows with the Microsoft compiler:
```sh
cl baklava.c
baklava.exe
```