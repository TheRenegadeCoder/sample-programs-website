---
title: Fizz Buzz in C#
layout: default
date: 2018-08-14
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-08-14

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 26 2019 00:00:41. The solution was first committed on Aug 14 2018 11:18:18. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).