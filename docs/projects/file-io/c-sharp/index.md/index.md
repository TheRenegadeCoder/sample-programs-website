# File Io in C#

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
using System;
using System.IO;

namespace SamplePrograms
{
    public class FileIO
    {
        public static void Write() =>
            File.WriteAllText("output.txt", "file contents");

        public static string Read() =>
            File.ReadAllText("output.txt");

        public static void Main(string[] args)
        {
            Write();
            Console.WriteLine(Read());
        }
    }
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.