---
authors:
- rzuckerm
date: 2023-12-09
featured-image: prime-number-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- octave
- prime-number
title: Prime Number in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/octave/how-to-implement-the-solution.md
- sources/programs/prime-number/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function prime_number()
    usage = 'Usage: please input a non-negative integer';
    arg_list = argv();
    nargin = length(arg_list);
    if nargin == 0
        disp(usage);
        return;
    end

    n = str2num(arg_list{1});
    if length(n) ~= 1 || mod(n, 1) ~= 0 || n < 0
        disp(usage);
        return;
    end

    isprime = 0;
    if n == 2
        isprime = 1;
    elseif n < 2 || rem(n, 2) == 0
        isprime = 0;
    else
        isprime = 1;
        q = sqrt(n);
        m = 3;
        while m <= q
            if rem(n, m) == 0
                isprime = 0;
                break;
            end
            m = m + 2;
        end
    end

    if isprime == 1
        disp('prime');
    else
        disp('composite');
    end
end

```

{% endraw %}

Prime Number in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).