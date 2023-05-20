---
title: Quick Sort in Java
layout: default
date: 2019-11-01
featured-image: quick-sort-in-every-language.jpg
last-modified: 2019-11-01

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.ArrayList;

public class QuickSort {

    public static void main(String[] args) {
        ArrayList<Integer> numList = new ArrayList<>();
        if (args.length < 1) {
            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        } else if (args[0].length() < 2) {
            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        } else {
            String[] stringList = args[0].split(",");
            if (stringList.length < 2) {
                System.out.println(
                        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
            } else {
                for (int i = 0; i < stringList.length; i++) {
                    numList.add(Integer.parseInt(stringList[i].trim()));
                }
                if (numList.size() < 2) {
                    System.out.println(
                            "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
                } else {
                    sort(numList, 0, numList.size() - 1);
                    String str = "";
                    for (int i = 0; i < numList.size() - 1; i++) {
                        str += String.valueOf(numList.get(i));
                        str += ", ";
                    }
                    str += String.valueOf(numList.get(numList.size() - 1));
                    System.out.println(str);
                }
            }
        }
    }

    public static int partition(ArrayList<Integer> arr, int low, int high) {
        int pivot = arr.get(high);
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr.get(j) <= pivot) {
                i++;
                int temp = arr.get(i);
                arr.set(i, arr.get(j));
                arr.set(j, temp);
            }
        }
        int temp = arr.get(i + 1);
        arr.set(i + 1, arr.get(high));
        arr.set(high, temp);
        return i + 1;
    }

    public static void sort(ArrayList<Integer> arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Sumathi Varadharajan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Nov 01 2019 00:48:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).