---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- java
- remove-all-whitespace
title: Remove All Whitespace in Java
title1: Remove All
title2: Whitespace in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/java/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class RemoveAllWhitespace {
    public static void main(String[] args) {
        if (args.length == 0 || args[0].isEmpty()) {
            showUsage();
        }

        System.out.println(removeAllWhitespace(args[0]));
    }

    private static void showUsage() {
        System.out.println("Usage: please provide a string");
        System.exit(1);
    }

    private static boolean isWhitespace(char c) {
        return switch (c) {
            case ' ', '\t', '\n', '\r' -> true;
            default -> false;
        };
    }

    private static String removeAllWhitespace(String input) {
        var result = new StringBuilder(input.length());

        for (char c : input.toCharArray()) {
            if (!isWhitespace(c)) {
                result.append(c);
            }
        }

        return result.toString();
    }
}
```

{% endraw %}

Remove All Whitespace in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).