---
authors:
- dyllew3
- Jeremy Grifski
date: 2019-10-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- capitalize
- java
title: Capitalize in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/java/how-to-implement-the-solution.md
- sources/programs/capitalize/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Capitalize {

    public static boolean isLetter(char someChar) {
        return (someChar >= 'a' && someChar <= 'z') || (someChar >= 'A' && someChar <= 'Z');
    }

    public static boolean isUpperCase(char someChar) {
        return (someChar >= 'A' && someChar <= 'Z');
    }

    public static void main(String[] args) {
        if (args.length == 0 || args[0].equals("")) {
            System.out.println("Usage: please provide a string");
            System.exit(1);
        }
        String sentence = args[0];

        char firstChar = sentence.charAt(0);
        if (isLetter(firstChar) && !isUpperCase(firstChar)) {
            char[] charArray = sentence.toCharArray();
            charArray[0] = Character.toUpperCase(firstChar);
            sentence = new String(charArray);
        }
        System.out.println(sentence);

    }
}

```

{% endraw %}

Capitalize in [Java](https://sampleprograms.io/languages/java) was written by:

- dyllew3
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).