---

title: Baklava in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Baklava in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).