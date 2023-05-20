---
title: Insertion Sort in Java
layout: default
date: 2019-10-15
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-10-15

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.ArrayList;

public class InsertionSort {

    public static void main(String[] args) {

        ArrayList<Integer> numList = new ArrayList<>();

        if (args.length < 1) {
            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        }

        else if (args[0].length() < 2) {

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
                    insertionSort(numList);
                }
            }

        }

    }

    public static void insertionSort(ArrayList<Integer> numList) {
        for (int j = 1; j < numList.size(); j++) {
            int k = j - 1, val = numList.get(j);
            while (k >= 0 && numList.get(k) > val) {

                numList.set(k + 1, numList.get(k));
                k--;
            }
            numList.set(k + 1, val);
        }
        for (int i = 0; i < numList.size() - 1; i++) {
            System.out.print(numList.get(i) + ", ");
        }
        System.out.print(numList.get(numList.size() - 1));

    }

}
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Java](https://sampleprograms.io/languages/java) was written by:

- Ganesh Naik
- Jeremy Grifski
- Shubham Raj

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 15 2019 00:10:22. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).