---

title: Baklava in Java
layout: default
date: 2022-04-28
last-modified: 2022-08-14

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
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

[Baklava](https://sampleprograms.io/projects/baklava) in [Java](https://sampleprograms.io/languages/java) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).