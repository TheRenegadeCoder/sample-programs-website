---

title: File Io in C++
layout: default
date: 2022-04-28
last-modified: 2022-05-16

---

Welcome to the [File Io](https://sampleprograms.io/projects/file-io) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <fstream>
#include <string>

void write_file()
{
    std::fstream out("output.txt", std::ios::out);

    if(!out.is_open())
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

    if(!in.is_open())
    {
        std::cout << "Could not open file!\n";
        return;
    }

    std::string line;
    while(std::getline(in, line))
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

[File Io](https://sampleprograms.io/projects/file-io) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Noah Nichols

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).