# Reverse String in C#

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
using System;

namespace SamplePrograms
{
    public class ReverseString
    {
        public static string Reverse(string input)
        {
            var charArray = input.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }

        public static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                System.Console.WriteLine(Reverse(args[0]));
            }
        }
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.