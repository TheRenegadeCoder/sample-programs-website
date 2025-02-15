---
authors:
- Jeremy Grifski
date: 2022-05-16
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2022-05-16
layout: default
tags:
- java
- longest-common-subsequence
title: Longest Common Subsequence in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/java/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class LongestCommonSubsequence {

    static ArrayList<String> split_strings(String str) {
        String word = "";
        char dl = ',';

        str = str + dl;

        ArrayList<String> substr_list = new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {

            if (str.charAt(i) != dl)
                word = word + str.charAt(i);
            else {
                if ((int) word.length() != 0)
                    substr_list.add(word);
                word = "";
            }
        }

        return substr_list;
    }

    static void longest_common_subsequence(ArrayList<String> arr1, ArrayList<String> arr2) {

        int[][] array = new int[arr1.size() + 1][arr2.size() + 1];

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {

                if (i == 0 || j == 0) {
                    array[i][j] = 0;
                } else if (arr1.get(i - 1).equals(arr2.get(j - 1))) {
                    array[i][j] = 1 + array[i - 1][j - 1];
                } else {
                    array[i][j] = Math.max(array[i - 1][j], array[i][j - 1]);
                }
            }
        }

        ArrayList<String> lcs = new ArrayList<>();
        int x = array.length - 1;
        int y = array[0].length - 1;

        while (x > 0 && y > 0) {

            if (arr1.get(x - 1).equals(arr2.get(y - 1))) {
                lcs.add(0, arr1.get(x - 1));
                x--;
                y--;
            } else {
                if (array[x - 1][y] > array[x][y - 1])
                    x--;
                else
                    y--;
            }
        }

        for (int element = 0; element < lcs.size() - 1; element++) {
            System.out.print(lcs.get(element) + ",");
        }
        System.out.println(lcs.get(lcs.size() - 1));
    }

    public static void main(String args[]) {

        if (args.length < 2 || args[0] == "" || args[1] == "") {
            System.out.println("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"");
            return;
        }

        ArrayList<String> arr1 = split_strings(args[0]);
        ArrayList<String> arr2 = split_strings(args[1]);

        longest_common_subsequence(arr1, arr2);
    }
}

```

{% endraw %}

Longest Common Subsequence in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).