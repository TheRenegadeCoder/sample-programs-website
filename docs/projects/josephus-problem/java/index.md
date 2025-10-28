---
authors:
- Apurva Vats
date: 2025-10-29
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- java
- josephus-problem
title: Josephus Problem in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/java/how-to-implement-the-solution.md
- sources/programs/josephus-problem/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class JosephusProblem {

    private static int josephus(int n, int k) {
        if (n == 1) return 1;
        return (josephus(n - 1, k) + k - 1) % n + 1;
    }

    public static void main(String[] args) {
        final String usage_msg = "Usage: please input the total number of people and number of people to skip.\n";

        if (args.length != 2) {
            System.err.print(usage_msg);
            System.exit(1);
        }

        int n=0, k=0;
        try {
            n = Integer.parseInt(args[0]);
            k = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.err.print(usage_msg);
            System.exit(1);
        }

        if (n <= 0 || k <= 0) {
            System.err.print(usage_msg);
            System.exit(1);
        }

        int result = josephus(n, k);
        System.out.println(result);
    }
}

```

{% endraw %}

Josephus Problem in [Java](https://sampleprograms.io/languages/java) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).