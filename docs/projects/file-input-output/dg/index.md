---
authors:
- Jeremy Grifski
- Riley Martine
date: 2018-10-03
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-10-10
layout: default
tags:
- dg
- file-input-output
title: File Input Output in Dg
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/dg/how-to-implement-the-solution.md
- sources/programs/file-input-output/dg/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Dg](https://sampleprograms.io/languages/dg) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dg
import '/os'

write_file = filename s ->
    except
        err =>
            open filename 'w' |>.write <| s
        err :: OSError =>
            print "Cannot open file" filename

read_file = filename ->
    except
        err =>
            with fd = open filename 'r' =>
                print $ fd.read!
        err :: OSError =>
            print "Cannot open file" filename


filename = "output.txt"
write_file filename "Example text"
read_file filename

```

{% endraw %}

File Input Output in [Dg](https://sampleprograms.io/languages/dg) was written by:

- Jeremy Grifski
- Riley Martine

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).