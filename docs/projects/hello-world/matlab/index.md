---

title: Hello World in MATLAB
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-matlab-featured-image.JPEG
tags: [matlab, hello-world]
author:
  - virtual_flat

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
disp('Hello, World!');
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Syntax in MATLAB is based on its MATLAB scripting language. At any rate, here
is what we are working with:

```matlab
fprintf("Hello, World!")
```

One line is all it takes! The "details-hidden" nature of the languages removes
the need to declare variables or classes before the fun begins. `fprintf` is the
command in MATLAB that formats data and displays it in the command window. In
this case, the data is the string "Hello, World!" (denoted by the
quotations).


## How to Run the Solution

Running our program is a relatively simple affair. First, the script must be
saved [using the MATLAB editor][1]. File > Save or CNTL+S will do the trick, and it
will generate a file with the extension \*.m (yep, only one character). After
that, hit run and watch as our polite greeting to our surroundings populates
the screen.

If you want to try this out yourself, you can get a 30 day free trial of MATLAB
R2018a (the most recent release at the time of this writing), download the .m
file and run the script! Note, if you are a university student, your school may
have licenses of MATLAB available to you.

Alternatively, you can try to use [Octave Online][2], an open-source alternative to
MATLAB. [According to its wiki page][3], Octave is mostly compatible with MATLAB.
In fact, our solution to Hello World in MATLAB works great.
