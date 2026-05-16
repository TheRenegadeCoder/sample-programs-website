---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-10
layout: default
tags:
- java
- zeckendorf
title: Zeckendorf in Java
title1: Zeckendorf
title2: in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/java/how-to-implement-the-solution.md
- sources/programs/zeckendorf/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;
import java.util.stream.Collectors;

public class Zeckendorf {
    public static void main(String[] args) {
        try {
            if (args.length == 0 || args[0].isBlank()) {
                throw new Exception();
            }

            long n = Long.parseLong(args[0].trim());
            if (n < 0) throw new Exception();

            if (n == 0) {
                System.out.println("");
                return;
            }

            System.out.println(formatResult(getZeckendorf(n)));

        } catch (Exception e) {
            System.out.println("Usage: please input a non-negative integer");
        }
    }

    private static List<Long> getZeckendorf(long target) {
        List<Long> fibs = new ArrayList<>();
        long a = 1;
        long b = 2;

        fibs.add(a);
        while (b <= target) {
            fibs.add(b);
            long next = a + b;
            a = b;
            b = next;
        }

        List<Long> selected = new ArrayList<>();
        long remaining = target;

        for (int i = fibs.size() - 1; i >= 0 && remaining > 0; i--) {
            long currentFib = fibs.get(i);

            if (currentFib <= remaining) {
                selected.add(currentFib);
                remaining -= currentFib;
                i--;
            }
        }

        return selected;
    }

    private static String formatResult(List<Long> result) {
        return result.stream().map(String::valueOf).collect(Collectors.joining(", "));
    }
}
```

{% endraw %}

Zeckendorf in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).