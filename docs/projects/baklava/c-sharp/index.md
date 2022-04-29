---

---

Welcome to the Baklava in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
﻿using System;

class CSharp
{

    static void Main (string[] args)
    {

        for (SByte i = 0; i < 10; i++)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

        for (SByte i = 10; -1 < i; i--)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

    }

}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.