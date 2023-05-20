---
title: File Input Output in Bash
layout: default
date: 2018-10-28
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-10-28

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).