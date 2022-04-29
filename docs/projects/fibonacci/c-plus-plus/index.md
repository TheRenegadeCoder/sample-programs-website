---

---

Welcome to the Fibonacci in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C++
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2 || std::string(argv[1]) == "")
  {
    cout << "Usage: please input the count of fibonacci numbers to output" << endl;
    return 1;
  }

  int n = atoi(argv[1]);
  if (n == 0 && std::string(argv[1]) != "0")
  {
    cout << "Usage: please input the count of fibonacci numbers to output" << endl;
    return 1;
  }
  int first = 0;
  int second = 1;
  int result = 0;

  for (int i = 1; i <= n; ++i)
  {
      result = first + second;
      first = second;
      second = result;
      cout << i << ": " << first << endl;
  }
  return 0;
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.