---

title: Palindromic Number in Java
layout: default
date: 2022-04-28
last-modified: 2022-07-03

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class PalindromicNumber {

    public static void main(String[] args) {
        Long num;
        try {
            num = Long.parseLong(args[0]);
        } catch (Exception ignored) {
            num = null;
        }

        if (num == null || num.toString().length() < 2) {
            System.out.println("Usage: please input a number with at least two digits");
        } else {
            System.out.println(isPalindromic(num));
        }
    }

    /**
     * Checks if the number is palindromic or not
     */
    public static boolean isPalindromic(Long num) {
        char[] numChars = String.valueOf(num).toCharArray();
        for (int i = 0; i < numChars.length / 2; i++) {
            if (numChars[i] != numChars[numChars.length - 1 - i])
                return false;
        }
        return true;
    }
}
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Java](https://sampleprograms.io/languages/java) was written by:

- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).