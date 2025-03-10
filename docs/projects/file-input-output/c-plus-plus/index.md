---
authors:
- Jeremy Grifski
- Noah Nichols
- rzuckerm
date: 2018-09-10
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- c-plus-plus
- file-input-output
title: File Input Output in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/file-input-output/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <fstream>
#include <string>

void write_file()
{
    std::fstream out("output.txt", std::ios::out);

    if (!out.is_open())
    {
        std::cout << "Could not open file!\n";
        return;
    }

    out << "A line of text\n";
    out << "Another line of text\n";

    out.flush();

    out.close();
}

void read_file()
{
    std::fstream in;

    in.open("output.txt", std::ios::in);

    if (!in.is_open())
    {
        std::cout << "Could not open file!\n";
        return;
    }

    std::string line;
    while (std::getline(in, line))
    {
        std::cout << line << "\n";
    }

    in.close();
}

int main()
{
    write_file();
    read_file();
}
```

{% endraw %}

File Input Output in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Noah Nichols

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's first take a look at the solution. Then, we'll walk through each line of
code:

In less than 50 lines, we have our solution!

### Includes

In our sample, we include three different standard library utilities:

```c++
#include <iostream>
#include <fstream>
#include <string>
```

Here, we can see that we include he standard I/O for printing messages onto the
screen, the standard file I/O for accessing files, and the C++ string library
for storing each line in the file.

### Writing to a File

From there, we defined the `write_file()` function which we'll use to write some
arbitrary text to a file:

```c++
void write_file()
{
    std::fstream out("output.txt", std::ios::out);

    if (!out.is_open())
    {
        std::cout << "Could not open file!\n";
        return;
    }

    out << "A line of text\n";
    out << "Another line of text\n";

    out.flush();

    out.close();
}
```

Inside this function, we begin by creating a `std::fstream` object called out:

```c++
std::fstream out("file.txt", std::ios::out);
```

One of the constructors in `std::fstream` takes a C-style string for the first
argument and something called a "mode". A mode in this context refers to how the
file will be opened. Will the file be opened for reading, writing, or even both?
Will reading/writing begin at the beginning of the file or the end?

In this constructor, the second argument defaults to both reading and writing.
We just want write abilities so we use `std::ios::out`. You can mix and match
different modes together with the bitwise operator `|` (OR).

Example: `std::fstream out_and_append("file.txt", std::ios::out | std::ios::app);`

Of course, there are other modes available which we can find in DevDocs C++ File
I/O documentation. At any rate, let's get back to the code:

```c++
if (!out.is_open())
{
    std::cout << "Could not open file!\n";
    return;
}
```

These five lines of code are basic error checking to make sure the file is
actually opened. Then, we push a couple of strings to our output file stream:

```c++
out << "A line of text\n";
out << "Another line of text\n";
```

Using a file stream in C++ is the same as using the standard output. However,
we'll need to make sure to do a few things before we're done:

```c++
out.flush();
out.close();
```

Before the function returns, we do a couple of maintenance related tasks. First,
we flush the buffer. Sometimes the function (or in our case, an operator) that
we call to write to the file doesn't immediately write them to disk. It may
still be in memory waiting to be written to the file. We call the method `flush`
to make sure everything in memory is written to disk.

Next, we close the file. This frees up resources that we are done using. It's a
good idea to always close a file when done. After all, if enough files are open,
the OS might complain and not allow us to open another file until some other
files have been closed. This is called the file descriptor limit and not closing
files and opening new ones over time can exhaust the number of file descriptors
available.

### Reading from a File

After we've implemented file writing, we can implement file reading:

```c++
void read_file()
{
    std::fstream in;

    in.open("output.txt", std::ios::in);

    if (!in.is_open())
    {
        std::cout << "Could not open file!\n";
        return;
    }

    std::string line;
    while (std::getline(in, line))
    {
        std::cout << line << "\n";
    }

    in.close();
}
```

Just like last time, we open the same file. However, this time we're opening it
for reading purposes. Then, we make sure the file is opened. If it isn't, we
print a message to the screen and return:

```c++
std::fstream in;

in.open("output.txt", std::ios::in);

if (!in.is_open())
{
    std::cout << "Could not open file!\n";
    return;
}
```

After that, we can begin reading:

```c++
std::string line;
while (std::getline(in, line))
{
    std::cout << line << "\n";
}
```

To start, we create an empty `std::string` and loop line by line in the file until
we reach EOF (end of file). `std::getline` takes a reference to a 
`std::basic_istream` which `std::fstream` inherits from. The second argument is a
reference to a `std::string`. It returns a reference to a `std::basic_istream`.

`std::basic_istream` inherits from `std::basic_ios` which overloads the `bool`
operator. This means we can use `std::getline` (or more precisely,
`std::basic_istream`) in boolean contexts such as while conditionals.

When we're done, we close the file and don't call flush because we just read
from the file and haven't written anything to it:

```c++
in.close();
```

And, that's how we read from a file in C++.

### The Main Function

As usual, C++ programs cannot be executed without a main function:

```c++
int main()
{
    write_file();
    read_file();
}
```

Here, we make a call to each function we've created: `write_file()` and
`read_file()`. And, that's it!


## How to Run the Solution

There are many online compilers such as Compiler Explorer that you can use to
compile C++ code. If you have a compiler installed on your system such g++ or
clang++ use the following commands:

```console
g++ -o program file.cpp
clang++ -o program file.cpp
```
And, that's it! You've successfully executed the solution.
