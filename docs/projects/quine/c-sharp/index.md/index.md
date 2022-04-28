# Quine in C#

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
class Quine { static void Main() { var s = "class Quine {{ static void Main() {{ var s = {0}{1}{0}; System.Console.WriteLine(s, (char)34, s); }} }}"; System.Console.WriteLine(s, (char)34, s); } }
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.