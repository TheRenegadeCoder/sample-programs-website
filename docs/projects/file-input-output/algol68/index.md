---
title: File Input Output in Algol68
layout: default
date: 2023-01-20
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-01-20

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC write file = (STRING file name) INT:
(
    FILE f;
    INT status := establish(f, file name, stand out channel);
    IF status /= 0
    THEN
        put(stand error, ("Cannot open ", file name, " for write", new line))
    ELSE
        put(f, ("Hello from Algol 68!", new line));
        put(f, ("Here is a line", new line));
        put(f, ("Here is another line", new line));
        put(f, ("Goodbye!", new line));
        close(f)
    FI;

    status
);

PROC read file = (STRING file name) INT:
(
    FILE f;
    INT status := open(f, file name, stand in channel);
    IF status /= 0
    THEN
        put(stand error, ("Cannot open ", file name, " for read", new line))
    ELSE
        on logical file end(f, (REF FILE inf) BOOL:
            (
                close(inf);
                done
            )
        );

        STRING line;
        DO
            get(f, (line, new line));
            write((line, new line))
        OD
    FI;

done:
    status
);

STRING file name := "output.txt";
IF write file(filename) /= 0
THEN
    stop
FI;

IF read file(filename) /= 0
THEN
    stop
FI
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 31 2023 21:43:37. The solution was first committed on Jan 20 2023 11:21:46. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).