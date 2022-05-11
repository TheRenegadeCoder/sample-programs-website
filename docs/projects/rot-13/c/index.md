---

title: Rot 13 in C
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Rot 13 in C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).