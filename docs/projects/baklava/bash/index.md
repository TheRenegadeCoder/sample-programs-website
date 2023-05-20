---
title: Baklava in Bash
layout: default
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

for i in {0..9}; do
    printf " %.0s" $(seq 1 $(( 10 - $i )))
    printf "*%.0s" $(seq 1 $(( $i * 2 + 1 )))
    echo
done

printf "*%.0s" {1..21}
echo

for i in {9..0}; do
    printf " %.0s" $(seq 1 $(( 10 - $i )))
    printf "*%.0s" $(seq 1 $(( $i * 2 + 1 )))
    echo
done
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 18 2019 16:44:21. The solution was first committed on Sep 17 2018 16:48:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).