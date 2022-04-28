# Baklava in D

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```D
import std.stdio, std.array;

void main (string[ ] args)
{

    for (byte i = 0; i < 10; i++)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

    for (byte i = 10; -1 < i; i--)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.