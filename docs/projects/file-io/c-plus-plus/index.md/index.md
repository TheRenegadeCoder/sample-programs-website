# File Io in C++

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C++
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.