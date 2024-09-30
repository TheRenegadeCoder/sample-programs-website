---
authors:
- Ashish Aggarwal
- Jeremy Grifski
- rzuckerm
date: 2020-10-05
featured-image: linear-search-in-every-language.jpg
last-modified: 2023-01-29
layout: default
tags:
- java
- linear-search
title: Linear Search in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/java/how-to-implement-the-solution.md
- sources/programs/linear-search/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class LinearSearch {

    public static void main(String[] args) {
        try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            Integer keyToSearch = Integer.parseInt(args[1]);
            String[] NumberArray = args[0].split(",");
            for (String Number : NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            if (listOfNumbers.size() >= 1) {
                StringBuilder output = new StringBuilder();
                Boolean searched = linearSearch(listOfNumbers, keyToSearch);
                System.out.println(searched);
            } else {
                System.out.println(
                        "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
            }
        } catch (Exception e) {
            System.out.println(
                    "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
        }
    }

    private static Boolean linearSearch(ArrayList<Integer> list, Integer keyToSearch) {
        Boolean ans = false;
        for (Integer number : list) {
            if (number == keyToSearch) {
                ans = true;
                break;
            }
        }
        return ans;
    }
}

```

{% endraw %}

Linear Search in [Java](https://sampleprograms.io/languages/java) was written by:

- Ashish Aggarwal
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).