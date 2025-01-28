---
authors:
- "Christoph B\xF6hmwalder"
- rzuckerm
date: 2018-09-04
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-28
layout: default
tags:
- fizz-buzz
- tex
title: Fizz Buzz in Tex
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/tex/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/tex/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Tex](https://sampleprograms.io/languages/tex) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tex
% Source: https://rosettacode.org/wiki/String_append#Plain_TeX
\def\addtomacro#1#2{\expandafter\def\expandafter#1\expandafter{#1#2}}

\newwrite\out
\immediate\openout\out=fizz-buzz.txt

\countdef\counter=1
\countdef\threecounter=2
\countdef\fivecounter=3
\counter=1
\threecounter=1
\fivecounter=1

\loop
    \def\printnum{1}
    \def\result{}
    \noindent
    \ifnum \threecounter>2
        \addtomacro\result{Fizz}
        \threecounter=0
        \def\printnum{0}
    \fi
    \ifnum \fivecounter>4
        \addtomacro\result{Buzz}
        \fivecounter=0
        \def\printnum{0}
    \fi
    \ifnum\printnum=1
        % print the counter variable
        \addtomacro\result{\the\counter}
    \fi
    \immediate\write\out{\result}
    \advance \counter 1
    \advance \threecounter 1
    \advance \fivecounter 1
\ifnum \counter<101
\repeat

\end

```

{% endraw %}

Fizz Buzz in [Tex](https://sampleprograms.io/languages/tex) was written by:

- Christoph Böhmwalder
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).