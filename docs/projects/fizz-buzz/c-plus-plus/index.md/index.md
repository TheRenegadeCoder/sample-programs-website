---

---

Welcome to the Fizz Buzz in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C++
#include <iostream>

int main()
{
    for (int i = 1; i <= 100; i++) {
        if (i % 15 == 0)
            std::cout << "FizzBuzz\n";
        else if (i % 5 == 0)
            std::cout << "Buzz\n";
        else if (i % 3 == 0)
            std::cout << "Fizz\n";
        else
            std::cout << i << "\n";
    }
    return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.