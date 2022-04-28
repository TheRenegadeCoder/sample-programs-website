---

---

Welcome to the Lcs in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
using System;
using System.Collections.Generic;
using System.Linq;

namespace SamplePrograms
{
    public class LongestCommonSubsequence
    {
        private static IEnumerable<string> LCS(IEnumerable<string> list1, IEnumerable<string> list2)
        {
            if (list1.Count() == 0 || list2.Count() == 0)
                return new List<string>();

            if (list1.First().Equals(list2.First()))
                return LCS(list1.Skip(1), list2.Skip(1)).Concat(new List<string>() { list1.First() });

            return Longest(LCS(list1, list2.Skip(1)), LCS(list1.Skip(1), list2));
        }

        private static IEnumerable<string> Longest(params IEnumerable<string>[] lists) =>
            lists.OrderByDescending(l => l.Count()).First();

        public static void Main(string[] args)
        {
            try
            {
                var list1 = args[0].Split(',').Select(i => i.Trim());
                var list2 = args[1].Split(',').Select(i => i.Trim());
                var lcs = LCS(list1, list2).Reverse();
                Console.WriteLine(string.Join(", ", lcs));
            }
            catch
            {
                Console.WriteLine("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"");
                Environment.Exit(1);
            }
        }
    }
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.