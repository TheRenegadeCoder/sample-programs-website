---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- java
- roman-numeral
title: Roman Numeral in Java
title1: Roman Numeral
title2: in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/java/how-to-implement-the-solution.md
- sources/programs/roman-numeral/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class RomanNumeral {
    private static final int[] ROMAN = new int[128];

    static {
        ROMAN['I'] = 1;
        ROMAN['V'] = 5;
        ROMAN['X'] = 10;
        ROMAN['L'] = 50;
        ROMAN['C'] = 100;
        ROMAN['D'] = 500;
        ROMAN['M'] = 1000;
    }

    public static void main(String[] args) {
        if (args.length == 0 || args[0] == null) {
            System.out.println("Usage: please provide a string of roman numerals");
            System.exit(1);
        }

        String s = args[0].toUpperCase();

        int result = romanToInt(s);
        if (result == -1) {
            System.err.println("Error: invalid string of roman numerals");
            System.exit(1);
        }

        System.out.println(result);
    }

    private static int romanToInt(String input) {
        if (input.isEmpty()) {
            return 0;
        }
        
        int total = 0;
        int prev = 0;

        for (int i = input.length() - 1; i >= 0; i--) {
            char c = input.charAt(i);

            if (c >= 128 || ROMAN[c] == 0) {
                return -1;
            }

            int cur = ROMAN[c];

            if (cur < prev) {
                total -= cur;
            } else {
                total += cur;
            }

            prev = cur;
        }

        return total;
    }
}
```

{% endraw %}

Roman Numeral in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).