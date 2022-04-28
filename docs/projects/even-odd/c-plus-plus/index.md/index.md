---

---

# Even Odd in C++

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C++
#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main(int argc, char **argv)
{
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0)) {
        cout<<"Usage: please input a number\n";
    } else {
        int input = atoi(argv[1]);
        if (input % 2 == 0) {
            cout<<"Even\n";
        }
        else {
            cout<<"Odd\n";
        }
    }

    return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.