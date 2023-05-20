---
title: File Input Output in Matlab
layout: default
date: 2020-10-02
featured-image: file-input-output-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
path = "output.txt";

% Write content to file
file = fopen(path,'w');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return
end
fprintf(file, "Hello, World!\n");
fclose(file);

% Read content from file
file = fopen(path,'r');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return
end
a = fscanf(file,'%s');
fprintf(a)
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- iwishiwasaneagle

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).