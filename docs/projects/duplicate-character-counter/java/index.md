---
title: Duplicate Character Counter in Java
layout: default
date: 2022-10-03
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2022-10-03

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class DuplicateCharacterCounter {
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
            Map<Character, Integer> map = new HashMap<>();
            for (Character c : inputStr.toCharArray()) {
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
            boolean flag = false;
            for (Character c : inputStr.toCharArray()) {
                if (map.get(c) > 1) {
                    flag = true;
                    System.out.printf("%c: %d\n", c, map.get(c));
                    map.put(c, 0);
                }
            }
            if (flag == false) {
                System.out.println("No duplicate characters");
            }
        }
    }
}
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 03 2022 20:20:06. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).