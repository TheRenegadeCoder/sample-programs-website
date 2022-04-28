# Fibonacci in C#

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
using System;

namespace SamplePrograms
{
    public class Fibonacci
    {
        public static void Main(string[] args)
        {
            try
            {
                int n = int.Parse(args[0]);
                int first = 0;
                int second = 1;
                int result = 0;
                for(int i = 1; i <= n; i++)
                {
                    result = first + second;
                    first = second;
                    second = result;
                    Console.WriteLine(i + ": " + first);
                }
            }
            catch(Exception)
            {
                Console.WriteLine("Usage: please input the count of fibonacci numbers to output");
                Environment.Exit(0);
            }
        }
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.