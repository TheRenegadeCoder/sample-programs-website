---
authors:
- Jeremy Grifski
- jsonW0
date: 2019-10-27
featured-image: rot13-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- java
- rot13
title: Rot13 in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/java/how-to-implement-the-solution.md
- sources/programs/rot13/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Rot13 {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: please provide a string to encrypt");
        } else {
            String code = args[0];
            String result = "";
            if (code.length() == 0) {
                System.out.println("Usage: please provide a string to encrypt");
            } else {
                String lower = "abcdefghijklmnopqrstuvwxyz";
                String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                for (int a = 0; a < code.length(); a++) {
                    String ch = code.substring(a, a + 1);
                    int l = lower.indexOf(ch);
                    int u = upper.indexOf(ch);
                    if (l != -1) {
                        result += lower.substring((l + 13) % 26, (l + 14) % 26 != 0 ? (l + 14) % 26 : l + 14);
                    } else if (u != -1) {
                        result += upper.substring((u + 13) % 26, (u + 14) % 26 != 0 ? (u + 14) % 26 : u + 14);
                    } else {
                        result += ch;
                    }
                }
                System.out.println(result);
            }
        }
    }
}
```

{% endraw %}

Rot13 in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- jsonW0

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).