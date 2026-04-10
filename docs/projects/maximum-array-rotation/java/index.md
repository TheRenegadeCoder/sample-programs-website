---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- java
- maximum-array-rotation
title: Maximum Array Rotation in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/java/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.Arrays;

public class MaximumArrayRotation {
    public static void main(String[] args) {
        int[] input = parse(args);
        System.out.println(maximumRotationSum(input));
    }

    private static void usage() {
        System.err.println("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")");
        System.exit(1);
    }

    private static int[] parse(String[] args) {
        if (args.length != 1 || args[0] == null || args[0].isBlank()) {
            usage();
        }

        try {
            int[] values = Arrays.stream(args[0].split(","))
                    .map(String::trim)
                    .mapToInt(Integer::parseInt)
                    .toArray();

            if (values.length == 0) {
                usage();
            }

            return values;

        } catch (NumberFormatException e) {
            usage();
            return new int[0]; // unreachable
        }
    }

    private static long maximumRotationSum(int[] values) {
        int n = values.length;
        if (n == 0) {
            usage();
        }

        long sum = 0;
        long currentSum = 0;

        for (int i = 0; i < n; i++) {
            sum += values[i];
            currentSum += (long) values[i] * i;
        }

        long maxSum = currentSum;

        for (int i = 1; i < n; i++) {
            currentSum += sum - (long) n * values[n - i];
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```

{% endraw %}

Maximum Array Rotation in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).