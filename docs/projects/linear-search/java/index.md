---
title: Linear Search in Java
layout: default
date: 2020-10-05
featured-image: linear-search-in-every-language.jpg
last-modified: 2020-10-05

---

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

[Linear Search](https://sampleprograms.io/projects/linear-search) in [Java](https://sampleprograms.io/languages/java) was written by:

- Ashish Aggarwal
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 29 2023 21:43:56. The solution was first committed on Oct 05 2020 19:35:45. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).