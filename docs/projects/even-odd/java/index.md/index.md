# Even Odd in Java

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.