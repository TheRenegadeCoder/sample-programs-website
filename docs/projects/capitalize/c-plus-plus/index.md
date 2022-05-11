---

title: Capitalize in C++
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Capitalize in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```c++
#include <iostream>
#include <cstring>

int main(int argc, const char *argv[])
{
    if (argc < 2 || argv[1][0] == '\0') { //If there is less than 2 arguments, no string was passed
        std::cout << "Usage: please provide a string";
        return 1;
    }
    
    for (int j = 0; j < (int) std::strlen(argv[1]); j++) { 
        if (j == 0)                                        
            std::cout << (char) toupper(argv[1][j]);      
        else
            std::cout << *(argv[1] + sizeof(char)*j);      
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).