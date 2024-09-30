---
authors:
- Jeremy Grifski
- smallblack9
date: 2020-10-11
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2022-10-11
layout: default
tags:
- java
- palindromic-number
title: Palindromic Number in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/java/how-to-implement-the-solution.md
- sources/programs/palindromic-number/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class PalindromicNumber {

    public static void main(String[] args) {
        Long num;
        try {
            num = Long.parseLong(args[0]);
        } catch (Exception ignored) {
            num = null;
        }

        if (num == null || num < 0) {
            System.out.println("Usage: please input a non-negative integer");
        } else {
            System.out.println(isPalindromic(num));
        }
    }

    public static boolean isPalindromic(Long num) {
        char[] numChars = String.valueOf(num).toCharArray();
        for (int i = 0; i < numChars.length / 2; i++) {
            if (numChars[i] != numChars[numChars.length - 1 - i])
                return false;
        }
        return true;
    }
}

```

{% endraw %}

Palindromic Number in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).