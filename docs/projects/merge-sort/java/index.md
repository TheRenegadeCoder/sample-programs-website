---
title: Merge Sort in Java
layout: default
date: 2019-10-17
featured-image: merge-sort-in-every-language.jpg
last-modified: 2019-10-17

---

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.ArrayList;

public class MergeSort {

    public static void main(String[] args) {

        ArrayList<Integer> numList = new ArrayList<>(); // creating an arraylist(for dynamic size) to store the numbers

        if (args.length < 1) { // null input
            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        }

        else if (args[0].length() < 2) { // checking for empty input and single number input

            System.out.println(
                    "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        } else {
            String[] stringList = args[0].split(","); // extract numbers from the passed string

            if (stringList.length < 2) { // wrong/invalid input format
                System.out.println(
                        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
            } else {

                for (int i = 0; i < stringList.length; i++) {
                    numList.add(Integer.parseInt(stringList[i].trim())); // convert to Int type and store in numList for
                                                                         // sorting
                }

                if (numList.size() < 2) { // wrong/invalid input format
                    System.out.println(
                            "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
                } else {
                    mergeSort(numList, 0, numList.size() - 1);

                    // display the sorted list to the user
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

    public static void mergeSort(ArrayList<Integer> numList, int low, int high) {

        if (low < high) {
            // calculating mid avoiding overflow
            int mid = low + (high - low) / 2;

            // recursively divide the list into 2 parts and call mergeSort on each half
            mergeSort(numList, low, mid);
            mergeSort(numList, mid + 1, high);

            // finally merge the sorted halves to get the final sorted list
            mergeList(numList, low, mid, high);

        }

    }

    public static void mergeList(ArrayList<Integer> numList, int low, int mid, int high) {

        int i = low;
        int j = mid + 1;
        int k = low;
        ArrayList<Integer> copyList = new ArrayList(numList);
        // find the smaller element using pointers,update the array and move the pointer
        // forward
        while (i <= mid && j <= high) { // till we don't reach the end of individual arrays

            if (copyList.get(i) <= copyList.get(j)) {
                numList.set(k, copyList.get(i));
                i++; // incrementing pointer
            } else {
                numList.set(k, copyList.get(j));
                j++; // incrementing pointer
            }

            k++; // incrementing arraylist index
        }

        // dealing with cases where we reach end of one part; just copy the remaining
        // part of second half
        while (i <= mid) {
            numList.set(k, copyList.get(i));
            i++;
            k++;
        }

        while (j <= high) {
            numList.set(k, copyList.get(j));
            j++;
            k++;
        }
    }

}
```

{% endraw %}

[Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Shubham Raj

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 17 2019 03:07:02. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).