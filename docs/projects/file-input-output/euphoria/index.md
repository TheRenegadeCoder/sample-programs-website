---

title: File Input Output in Euphoria
layout: default
date: 2022-04-28
last-modified: 2023-02-20

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
constant false = 0
constant true = 1

function write_file(sequence filename)
    integer fn = open(filename, "w")
    if fn < 0
    then
        printf(STDERR, "Cannot open %s for write\n", {filename})
        return false
    end if

    puts(fn, "Hello from Euphoria!\n")
    puts(fn, "This is a line\n")
    puts(fn, "This is another line\n")
    puts(fn, "Goodbye!\n")
    close(fn)
    return true
end function

function read_file(sequence filename)
    integer fn = open(filename, "r")
    if fn < 0
        then
        printf(STDERR, "Cannot open %s for read\n", {filename})
        return false
    end if

    object line
    while 1
    do
        line = gets(fn)
        if atom(line)
        then
            exit
        end if

        puts(STDOUT, line)
    end while

    close(fn)
    return true
end function

constant filename = "output.txt"
if write_file(filename)
then
    read_file(filename)
end if
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).