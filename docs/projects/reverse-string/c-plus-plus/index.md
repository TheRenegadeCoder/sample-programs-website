---

title: Reverse String in C++

---

Welcome to the Reverse String in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C++
#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char *argv[])
{
    if(argc < 2)
        return 0;
    
    std::string s = argv[1];
    std::reverse(s.begin(), s.end());

    std::cout << s << "\n";
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.