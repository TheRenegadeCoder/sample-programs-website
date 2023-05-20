---
title: Josephus Problem in Python
layout: default
date: 2022-12-30
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2022-12-30

---

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys  # for receiving inputs from command line

def josephus(n, k): # main routine
  if (n == 1):
    return 1
  else:
    return (josephus(n - 1, k) + k-1) % n + 1

n, k = 0, 0  # initialising the values 

try:
  n = int(sys.argv[1])  # input from CLI
  k = int(sys.argv[2])  # input from CLI

except:
  print("Usage: please input the total number of people and number of people to skip.")
  exit(1)

if (n <= k):
    print("Usage: please input the total number of people and number of people to skip.")
    exit(1)

print(josephus(n, k))
```

{% endraw %}

[Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Python](https://sampleprograms.io/languages/python) was written by:

- Sriniketh J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).