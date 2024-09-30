---
authors:
- Jeremy Grifski
- Parker Johansen
date: 2018-12-30
featured-image: even-odd-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- even-odd
- java
title: Even Odd in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/java/how-to-implement-the-solution.md
- sources/programs/even-odd/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class EvenOdd {
    public static void verifyNumber(String n) throws NumberFormatException {
        if (n.startsWith("-"))
            n = n.substring(1);
        char[] nArray = n.toCharArray();
        for (char c : nArray) {
            if (!Character.isDigit(c))
                throw new NumberFormatException();
        }
    }

    public static void ErrorAndExit() {
        System.out.println("Usage: please input a number");
        System.exit(1);
    }

    public static void main(String[] args) {
        try {
            String nstr = args[0].trim();
            verifyNumber(nstr);
            String lastDigit = nstr.substring(nstr.length() - 1);
            int n = Integer.parseInt(lastDigit);
            String result = n % 2 == 0 ? "Even" : "Odd";
            System.out.println(result);
        } catch (NumberFormatException | ArrayIndexOutOfBoundsException | StringIndexOutOfBoundsException e) {
            ErrorAndExit();
        }
    }
}

```

{% endraw %}

Even Odd in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).