---
title: Longest Word in Java
layout: default
date: 2022-10-03
featured-image: longest-word-in-every-language.jpg
last-modified: 2022-10-03

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

class LongestWord {
    public static void error() {
        System.out.println("Usage: please provide a string");
    }

    public static void main(String[] args) {
        if (args.length <= 0) {
            error();
        } else if (args[0].length() == 0) {
            error();
        } else {
            String inputStr = args[0];
            String[] words = inputStr.split("\\s+");
            int max = -1;
            for (String word : words) {
                if (word.length() > max) {
                    max = word.length();
                }
            }
            System.out.println(max);
        }
    }
}
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 03 2022 21:33:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).