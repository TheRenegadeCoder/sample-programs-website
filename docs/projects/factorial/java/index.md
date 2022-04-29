---

title: Factorial in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Factorial in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Java
public class Factorial
{
    public static long fact(long n)
    {
        if (n <= 0)
            return 1;
        return n * fact(n - 1);
    }

    public static void main(String[] args)
    {
        try
        {
            long n = Long.parseLong(args[0]);
            if (n > 59)
            {
                System.out.println(String.format("%1$s! is out of the reasonable bounds for calculation.", n));
                System.exit(1);
            }
            else if (n < 0)
            {
                System.out.println("Usage: please input a non-negative integer");
                System.exit(1);
            }
            long result = fact(n);
            System.out.println(result);
        }
        catch (Exception e)
        {
            System.out.println("Usage: please input a non-negative integer");
            System.exit(1);
        }
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.