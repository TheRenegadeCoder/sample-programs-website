---
title: Factorial in Java
layout: default
date: 2018-12-30
featured-image: factorial-in-every-language.jpg
last-modified: 2018-12-30

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Factorial {
    public static long fact(long n) {
        if (n <= 0)
            return 1;
        return n * fact(n - 1);
    }

    public static void main(String[] args) {
        try {
            long n = Long.parseLong(args[0]);
            if (n > 59) {
                System.out.println(String.format("%1$s! is out of the reasonable bounds for calculation.", n));
                System.exit(1);
            } else if (n < 0) {
                System.out.println("Usage: please input a non-negative integer");
                System.exit(1);
            }
            long result = fact(n);
            System.out.println(result);
        } catch (Exception e) {
            System.out.println("Usage: please input a non-negative integer");
            System.exit(1);
        }
    }
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Java](https://sampleprograms.io/languages/java) was written by:

- Bharath
- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Dec 30 2018 17:30:18. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).