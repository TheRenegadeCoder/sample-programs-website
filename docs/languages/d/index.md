---
authors:
- GitHub Actions
date: 2018-05-06
featured-image: programming-languages.jpg
last-modified: 2025-03-25
layout: default
tags:
- d
title: The D Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/d/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the D page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- GitHub Actions

## Description

If you haven't heard of [D][1], I'm hardly surprised. After all, it's 
not exactly a popular language. In fact, it currently ranks 39th by 
popularity on GitHub. For reference, languages ahead of D include 
[Visual Basic .NET][2] (31st), [Haskell][3] (21st), [Swift][4] (18th), and [C][5] (8th). 
Meanwhile, D sits narrowly ahead of newer languages like [Julia][6] (43rd) 
and [Elixir][7] (45th).

That said, according to [Wikipedia][1], D is still a pretty interesting 
language. As you can probably imagine, D is supposed to be an 
improvement on C++. Apparently, the designers weren't a fan of the 
practical issues surrounding C++ (surprise, surprise!). As a result, 
D includes features like design by contract, garbage collection, 
associative arrays, array slicing, and lazy evaluation.

Perhaps the most interesting feature to me has to be the inline 
assembler. Apparently, developers can write assembly code directly 
in D source code:

```d
void *pc;
asm
{
    pop  EBX         ;
    mov  pc[EBP], EBX ; 
}
```

By adding an asm block, developers can quickly tap into the hardware 
with assembly code. Now, I think that is a pretty cool programming 
language feature.

[1]: https://en.wikipedia.org/wiki/D_(programming_language)
[2]: https://en.wikipedia.org/wiki/Visual_Basic_(.NET)
[3]: https://en.wikipedia.org/wiki/Haskell
[4]: https://en.wikipedia.org/wiki/Swift_(programming_language)
[5]: https://en.wikipedia.org/wiki/C_(programming_language)
[6]: https://en.wikipedia.org/wiki/Julia_(programming_language)
[7]: https://en.wikipedia.org/wiki/Elixir_(programming_language)


## Articles

There are 4 articles:

- [Baklava in D](https://sampleprograms.io/projects/baklava/d)
- [Factorial in D](https://sampleprograms.io/projects/factorial/d)
- [Fizz Buzz in D](https://sampleprograms.io/projects/fizz-buzz/d)
- [Hello World in D](https://sampleprograms.io/projects/hello-world/d)