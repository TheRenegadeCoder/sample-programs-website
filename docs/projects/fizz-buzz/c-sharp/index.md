---

title: Fizz Buzz in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Fizz Buzz in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
namespace FizzBuzz
{
    public class Program
    {
        public static string FizzBuzz(int number)
        {
            string temp = "";
            if (number % 3 == 0)
            {
                temp += "Fizz";
            }
            if (number % 5 == 0)
            {
                temp += "Buzz";
            }
            if (string.IsNullOrEmpty(temp))
            {
                temp += number;
            }
            return temp;
        }

        private static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                string line = FizzBuzz(i);
                System.Console.WriteLine(line);
            }
        }
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.