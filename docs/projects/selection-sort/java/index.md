---
authors:
- Jeremy Grifski
- Tim Lange
date: 2019-10-15
featured-image: selection-sort-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- java
- selection-sort
title: Selection Sort in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/java/how-to-implement-the-solution.md
- sources/programs/selection-sort/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.ArrayList;

public class SelectionSort {

    public static void main(String[] args) {
        try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            String[] NumberArray = args[0].split(",");
            for (String Number : NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            if (listOfNumbers.size() >= 2) {
                StringBuilder output = new StringBuilder();
                ArrayList<Integer> SortedList = sort(listOfNumbers);

                for (Integer Number : SortedList) {
                    if (SortedList.indexOf(Number) == 0) {
                        output.append(Number);
                    } else {
                        output.append(", ").append(Number);
                    }
                }
                System.out.println(output);
            } else {
                System.out.println(
                        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
            }
        } catch (Exception e) {
            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        }
    }

    private static ArrayList<Integer> sort(ArrayList<Integer> list) {
        for (int i = 0; i < list.size() - 1; i++) {
            for (int j = i + 1; j < list.size(); j++) {
                if (list.get(j) < list.get(i)) {
                    int memory = list.get(i);
                    list.set(i, list.get(j));
                    list.set(j, memory);
                }
            }
        }
        return list;
    }
}
```

{% endraw %}

Selection Sort in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Tim Lange

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).