---

title: File Io in Bash
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the File Io in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

read_file () {
  cat output.txt
}

write_file () {
    echo -e "$1" > output.txt
}

write_file "File text line 1\nFile text line 2\nFile text line 3"
read_file
```

{% endraw %}

File Io in Bash was written by:

- Parker Johansen

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).