---

title: Even Odd in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Java
public class EvenOdd
{
    public static void verifyNumber(String n) throws NumberFormatException
    {
        if (n.startsWith("-"))
            n = n.substring(1);
        char[] nArray = n.toCharArray();
        for (char c : nArray)
        {
            if (!Character.isDigit(c))
                throw new NumberFormatException();
        }
    }

    public static void ErrorAndExit()
    {
        System.out.println("Usage: please input a number");
        System.exit(1);
    }

    public static void main(String[] args)
    {
        try
        {
            String nstr = args[0].trim();
            verifyNumber(nstr);
            String lastDigit = nstr.substring(nstr.length() - 1);
            int n = Integer.parseInt(lastDigit);
            String result = n % 2 == 0 ? "Even" : "Odd";
            System.out.println(result);
        }
        catch (NumberFormatException | ArrayIndexOutOfBoundsException | StringIndexOutOfBoundsException e)
        {
            ErrorAndExit();
        }
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).