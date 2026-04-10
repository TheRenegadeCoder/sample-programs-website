---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- java
- maximum-subarray
title: Maximum Subarray in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/java/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.Arrays;

public class MaximumSubarray {

    public static void main(String[] args) {
        int[] input = parse(args);
        System.out.println(maximumSubarraySum(input));
    }

    private static void usage() {
        System.err.println("Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"");
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


    private static long maximumSubarraySum(int[] numbers) {
        if (numbers.length == 0) {
            return 0;
        }

        int currentSum = numbers[0];
        int maxSum = numbers[0];

        for (int i = 1; i < numbers.length; i++) {
            int number = numbers[i];
            currentSum = Math.max(number, currentSum + number);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```

{% endraw %}

Maximum Subarray in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).