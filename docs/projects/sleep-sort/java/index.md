---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- java
- sleep-sort
title: Sleep Sort in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/java/how-to-implement-the-solution.md
- sources/programs/sleep-sort/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.time.Duration;
import java.util.*;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class SleepSort {

    public static void main(String[] args) {
        if (args.length != 1 || args[0].isBlank()) {
            usage();
        }

        List<Integer> numbers = parse(args[0]);
        if (numbers.size() < 2) {
            usage();
        }

        List<Integer> sorted = sleepSort(numbers);

        System.out.println(format(sorted));
    }

    private static List<Integer> sleepSort(List<Integer> input) {
        List<Integer> sortedList = Collections.synchronizedList(new ArrayList<>());

        ExecutorService executor = Executors.newCachedThreadPool();

        CountDownLatch latch = new CountDownLatch(input.size());

        for (int n : input) {
            executor.submit(() -> {
                try {
                    Thread.sleep(n * 100L);
                    sortedList.add(n);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    latch.countDown();
                }
            });
        }

        try {
            latch.await();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        executor.shutdown();

        return sortedList;
    }

    private static List<Integer> parse(String input) {
        try {
            return Arrays.stream(input.split(",")).map(String::trim).map(Integer::parseInt).toList();
        } catch (Exception e) {
            usage();
            return List.of(); // Unreachable
        }
    }

    private static String format(List<Integer> list) {
        return list.stream().map(String::valueOf).collect(Collectors.joining(", "));
    }

    private static void usage() {
        System.out.println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        System.exit(1);
    }
}
```

{% endraw %}

Sleep Sort in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).