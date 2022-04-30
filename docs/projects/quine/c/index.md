---

title: Quine in C
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Quine in C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C
#include "stdio.h"
int main() { char* s="#include %cstdio.h%c%cint main() { char* s=%c%s%c; printf(s,34,34,10,34,s,34,10); return 0; }%c"; printf(s,34,34,10,34,s,34,10); return 0; }
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).