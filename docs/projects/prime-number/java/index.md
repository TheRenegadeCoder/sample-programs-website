---
authors:
- Ewerton Queiroz
- Ganesh Naik
- Jeremy Grifski
- Juan D Frias
date: 2019-10-10
featured-image: prime-number-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- java
- prime-number
title: Prime Number in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/java/how-to-implement-the-solution.md
- sources/programs/prime-number/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
class PrimeNumberException extends Exception {
}

public class PrimeNumber {

    public static boolean isPrime(int number) {
        if ((number % 2 == 0 && number != 2) || number == 1) {
            return false;
        }

        boolean foundFactor = false;
        for (int n = 3; n <= (int) Math.ceil(Math.sqrt(number)); ++n) {
            if ((number % n) == 0) {
                foundFactor = true;
                break;
            }
        }
        return !foundFactor;
    }

    public static void main(String[] args) {
        try {

            if (args.length < 1 || args[0].indexOf('-') != -1) {
                throw new PrimeNumberException();
            }

            if (isPrime(Integer.valueOf(args[0]))) {
                System.out.println("Prime");

            } else {
                System.out.println("Composite");
            }

        } catch (NumberFormatException | PrimeNumberException e) {
            System.err.println("Usage: please input a non-negative integer");
        }
    }
}

```

{% endraw %}

Prime Number in [Java](https://sampleprograms.io/languages/java) was written by:

- Ewerton Queiroz
- Ganesh Naik
- Jeremy Grifski
- Juan D Frias

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).