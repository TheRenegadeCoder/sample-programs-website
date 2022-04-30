---

title: Rot 13 in Python
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Rot 13 in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Python
import sys
from string import ascii_uppercase, ascii_lowercase


def rot_13(string):
    return ''.join([encrypt_char(c) for c in string])


def encrypt_char(c):
    if c in ascii_uppercase:
        ltrs = ascii_uppercase
    elif c in ascii_lowercase:
        ltrs = ascii_lowercase
    else:
        return c
    new_index = (ltrs.index(c) + 13) % 26
    return ltrs[new_index]


def exit_with_error():
    print('Usage: please provide a string to encrypt')
    sys.exit(1)


def main(args):
    try:
        string = args[0]
        if len(string) <= 0:
            exit_with_error()
        print(rot_13(string))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).