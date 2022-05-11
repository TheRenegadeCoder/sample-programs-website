---

title: Baklava in C++
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Baklava in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
  int i,j,k,n;
  n = 21;
  for(i=1; i<=(n+1)/2; )
    {
      for(k=1; (n+1)/2-i>=k; k++)
        cout<<" ";
      for(j=1; j<2*i; j++)
        cout<<"*";
      cout<<"\n";
      i++;
    }
  if(2*i-1>=n)
    {
      for(i=(n+1)/2-1; i>=1; i--)
        {
          for(k=1; (n+1)/2-i>=k; k++)
            cout<<" ";
          for(j=1; j<2*i; j++)
            cout<<"*";
          cout<<"\n";
        }
    }
  return(0);
}
```

{% endraw %}

Baklava in C++ was written by:

- yottanami
- Behnam Ahmad khan beigi

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 14 2019 10:52:47. The solution was first committed on Oct 09 2019 12:45:32. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).