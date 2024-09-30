---
authors:
- Jeremy Grifski
- Parker Johansen
date: 2018-12-30
featured-image: baklava-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- baklava
- java
title: Baklava in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/java/how-to-implement-the-solution.md
- sources/programs/baklava/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Baklava {
    public static void up() {
        for (int i = 0; i < 10; i++)
            printRow(i);
    }

    public static void down() {
        for (int i = 10; i >= 0; i--)
            printRow(i);
    }

    public static void printRow(int rowNum) {
        for (int j = 10 - rowNum; j > 0; j--)
            System.out.print(" ");
        for (int j = 0; j <= rowNum * 2; j++)
            System.out.print("*");
        System.out.println();
    }

    public static void main(String[] args) {
        up();
        down();
    }
}

```

{% endraw %}

Baklava in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).