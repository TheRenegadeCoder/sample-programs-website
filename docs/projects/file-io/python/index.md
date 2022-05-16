---

title: File Io in Python
layout: default
date: 2022-04-28
last-modified: 2022-05-16

---

Welcome to the [File Io](https://sampleprograms.io/projects/file-io) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
def write_file():
    try:
        with open("output.txt", "w") as out:
            out.write("Hi! I'm a line of text in this file!\n")
            out.write("Me, too!\n")
    except OSError as e:
        print(f"Cannot open file: {e}")
        return


def read_file():
    try:
        with open("output.txt", "r") as in_file:
            for line in in_file:
                print(line.strip())
    except OSError as e:
        print(f"Cannot open file to read: {e}")
        return


if __name__ == '__main__':
    write_file()
    read_file()
```

{% endraw %}

[File Io](https://sampleprograms.io/projects/file-io) in [Python](https://sampleprograms.io/languages/python) was written by:

- Ganesh Naik
- Jeremy Grifski
- Noah Nichols

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 22:17:17. The solution was first committed on Sep 12 2018 13:00:03. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).