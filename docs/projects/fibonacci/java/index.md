---

title: Fibonacci in Java
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Fibonacci {

    public static void main(String[] args) {
        try {
            int n = Integer.parseInt(args[0]);
            int first = 0;
            int second = 1;
            int result = 0;
            for (int i = 1; i <= n; i++) {
                result = first + second;
                first = second;
                second = result;
                System.out.println(i + ": " + first);
            }
        }
        catch(Exception e) {
            System.out.println("Usage: please input the count of fibonacci numbers to output");
            System.exit(1);
        }
    }

}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Java](https://sampleprograms.io/languages/java) was written by:

- Parker Johansen
- Marius

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2019 00:40:32. The solution was first committed on Oct 03 2018 13:08:02. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).