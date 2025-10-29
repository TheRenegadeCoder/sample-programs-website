---
authors:
- Apurva Vats
date: 2025-10-30
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- java
- longest-palindromic-substring
title: Longest Palindromic Substring in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/java/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class LongestPalindromicSubstring {

    private static final String usage_msg = "Usage: please provide a string that contains at least one palindrome\n";

    private static int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    private static boolean longestPalindromicSubstring(String s, StringBuilder result) {
        if (s == null || s.isEmpty()) {
            result.setLength(0);
            return false;
        }

        int start = 0, maxLength = 0;
        int len = s.length();

        for (int i = 0; i < len; i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int currLen = Math.max(len1, len2);

            if (currLen > maxLength) {
                start = i - (currLen - 1) / 2;
                maxLength = currLen;
            }
        }

        if (maxLength > 1) {
            result.setLength(0);
            result.append(s.substring(start, start + maxLength));
            return true;
        }

        result.setLength(0);
        return false;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.print(usage_msg);
            System.exit(1);
        }

        String input = args[0];
        StringBuilder result = new StringBuilder();

        if (longestPalindromicSubstring(input, result) && result.length() > 0) {
            System.out.println(result);
        } else {
            System.out.print(usage_msg);
        }
    }
}

```

{% endraw %}

Longest Palindromic Substring in [Java](https://sampleprograms.io/languages/java) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).