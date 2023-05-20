---
title: Longest Palindromic Substring in Python
layout: default
date: 2020-10-26
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2020-10-26

---

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

errorMessage = "Usage: please provide a string that contains at least one palindrome"

def longestPalindrome(string):
    longest = ""
    string = string.lower()

    centres = [len(string) - 1]
    for diff in range(1, len(string)):
        centres.append(centres[0] + diff)
        centres.append(centres[0] - diff)

    for centre in centres:
        if (min(centre + 1, 2 * len(string) - 1 - centre) <= len(longest)):
            break
        if centre % 2 == 0:
            left, right = (centre // 2) - 1, (centre // 2) + 1
        else:
            left, right = centre // 2, (centre // 2) + 1

        while left >= 0 and right < len(
                string) and string[left] == string[right]:
            left -= 1
            right += 1

        if right - left > len(longest):
            longest = string[left + 1:right]

    return longest


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print(errorMessage)
    else:
        string = sys.argv[1]
        if string == "" or string == None:
            print(errorMessage)
        sub = longestPalindrome(string)
        if len(sub) == 1:
            print(errorMessage)
        else:
            print(sub)
```

{% endraw %}

[Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Python](https://sampleprograms.io/languages/python) was written by:

- izexi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).