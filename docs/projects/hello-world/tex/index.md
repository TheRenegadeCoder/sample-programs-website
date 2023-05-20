---
title: Hello World in Tex
layout: default
last-modified: 2020-09-30
featured-image: hello-world-in-tex.jpg
tags: [tex, hello-world]
authors:
  - bracciata

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Tex](https://sampleprograms.io/languages/tex) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tex
%&pdftex

Hello, World!
\end
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Tex](https://sampleprograms.io/languages/tex) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Sep 04 2018 11:11:25. The solution was first committed on Aug 28 2018 15:40:04. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's dive right into Hello World in Tex.

It is much simpler in Tex due to the fact the Tex is a markup language.

```tex
%&pdftex
```

This first line is a declaring line used to explain that the desired output of this tex file is a pdf.

```tex
Hello, World!
```

This is the body better known as what will be displayed. You could replace that text with anything to have it show up.

```tex
\end
```

Finally, this is saying the document has ended by declaring (`\`) an `end`.


## How to Run the Solution

There are many options for running Tex files both online and offline. This said my personal favorite option is running it online through [Overleaf][1]. They even cover the other options including themselves on their website [here][2].

[1]: https://www.overleaf.com/
[2]: https://www.overleaf.com/learn
