---
title: Rot13 in C
layout: default
date: 2019-10-09
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-09

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void rot13(char *str) {
    for(int i = 0; str[i] != '\0'; i++) {
        char c = *(str + i);
        if(('a' <= c && 'n' > c) || ('A' <= c && 'N' > c)) {
            *(str + i) += 13;
        } else if(('n' <= c && 'z' >= c) || ('N' <= c && 'Z' >= c)) {
            *(str + i) -= 13;
        }
    }
}

int main(int argc, char *argv[]) {
    if(argc == 2 && strlen(argv[1]) != 0 && !isdigit(*argv[1])) {
        rot13(argv[1]);
        printf("%s\n", argv[1]);
    } else {
        printf("Usage: please provide a string to encrypt\n");
    }
    
    return 0;
}
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [C](https://sampleprograms.io/languages/c) was written by:

- Softizo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2019 20:06:02. The solution was first committed on Oct 09 2019 18:23:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).