---

---

# Baklava in Java

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Java
public class Baklava
{
    public static void up()
    {
        for (int i = 0; i < 10; i++)
            printRow(i);
    }

    public static void down()
    {
        for (int i = 10; i >= 0; i--)
            printRow(i);
    }

    public static void printRow(int rowNum)
    {
        for (int j = 10-rowNum; j > 0; j--)
            System.out.print(" ");
        for (int j = 0; j <= rowNum*2; j++)
            System.out.print("*");
        System.out.println();
    }

    public static void main(String[] args)
    {
        up();
        down();
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.