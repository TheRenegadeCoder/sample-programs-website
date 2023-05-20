---
title: Fibonacci in Java
layout: default
date: 2018-10-03
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-03

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
        } catch (Exception e) {
            System.out.println("Usage: please input the count of fibonacci numbers to output");
            System.exit(1);
        }
    }

}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Marius
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 03 2018 13:08:02. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).