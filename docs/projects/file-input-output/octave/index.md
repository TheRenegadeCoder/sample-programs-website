---
authors:
- iwishiwasaneagle
- rzuckerm
date: 2020-10-02
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- file-input-output
- octave
title: File Input Output in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/octave/how-to-implement-the-solution.md
- sources/programs/file-input-output/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
path = "output.txt";

% Write content to file
file = fopen(path,'w');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return;
end
fprintf(file, "Hello, World!\n");
fprintf(file, "Goodbye!\n");
fclose(file);

% Read content from file
file = fopen(path,'r');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return;
end
a = fgetl(file);
while ischar(a)
    disp(a);
    a = fgetl(file);
end
fclose(file);

```

{% endraw %}

File Input Output in [Octave](https://sampleprograms.io/languages/octave) was written by:

- iwishiwasaneagle
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).