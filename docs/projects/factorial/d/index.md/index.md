---

---

# Factorial in D

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```D


// Factorial program in D


import std.stdio: writeln;
import std.getopt;
int fac(int a)
{
  if (a <= 1)
    {
      return 1;
    }
  return a*fac(a-1);
}
int main(string[] args)
{
  int depth;
  auto params = getopt(args, "depth", &depth);
  int result = fac(depth);
  writeln(result);
  return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.