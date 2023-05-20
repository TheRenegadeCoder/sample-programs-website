---
title: Rot13 in Java
layout: default
date: 2019-10-27
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-27

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Rot13 {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: please provide a string to encrypt");
        } else {
            String code = args[0];
            String result = "";
            if (code.length() == 0) {
                System.out.println("Usage: please provide a string to encrypt");
            } else {
                String lower = "abcdefghijklmnopqrstuvwxyz";
                String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                for (int a = 0; a < code.length(); a++) {
                    String ch = code.substring(a, a + 1);
                    int l = lower.indexOf(ch);
                    int u = upper.indexOf(ch);
                    if (l != -1) {
                        result += lower.substring((l + 13) % 26, (l + 14) % 26 != 0 ? (l + 14) % 26 : l + 14);
                    } else if (u != -1) {
                        result += upper.substring((u + 13) % 26, (u + 14) % 26 != 0 ? (u + 14) % 26 : u + 14);
                    } else {
                        result += ch;
                    }
                }
                System.out.println(result);
            }
        }
    }
}
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- jsonW0

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 27 2019 22:01:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).