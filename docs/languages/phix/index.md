---
title: The Phix Programming Language
layout: default
date: 2023-04-16
last-modified: 2023-04-16
featured-imaged: programming-languages.jpg
tags: [phix]
authors:
  - rzuckerm

---

Welcome to the Phix page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

According to the [Phix Official Site][1], the aims of Phix are as follows:

* Create programs that are easy to write and maintain.
* Make it easier to find the location of compile-time and run-time errors
  (the official site says "bugs", but I think this is the actually intent).
* Allow programmers to focus on solutions instead of solving the solution.
* Create programs that are easy to read and understand.

Phix was created by [Pete Lomax][2]. Phix is largely based on [Euphoria][5]
and is almost [completely compatible][6] with Euphoria. Pete has this to say
as to [why he created this language][1]:

> Phix was born out of frustration at waiting 18 months for a new release, only
to find the problem was still there.

You may be wondering as to the reason for this name. According to the
[Phix Official Site][1]:

> Phix is Pete’s Self Hosted Hybrid Interpreter/Compiler. pshhic was not the
best of acronyms, plus phiX is the name of the first ever manmade lifeform
artifically created from scratch in a laboratory, which seems rather appropriate
for a self-hosted compiler

Phix has the same four data types as Euphoria:

* `object` - Base data type
* `atom` - A 31-bit signed integer or 64-bit floating point number depending upon the
  value stored. This is actually called `number` in the [official documentation][4],
  but `atom` is still accepted.
* `integer` - A 31-bit in signed integer
* `sequence` - A list of values. This list can be comprised of `atom`s (`number`s) or
  other `sequence`s

However, it adds a [fifth data type][4]:

* `string` - A `sequence` of characters or raw binary data

Unlike Euphoria, Phix provides [short-circuited ternary operators][7]. For
example, the [iif function][8] in Euphoria will evaluate both the true and false
expressions and select the appropriate value. In other words, this code in
Euphoria will call both `foo` and `bar` and then return the value to `x`
depending upon whether `x` is non-zero or not:

```euphoria
integer foo_or_bar = iff(x, foo(), bar())
```

In Phix, this can be written like this:

```phix
integer foo_or_bar = iff(x ? foo() : bar())
```

Only if `x` is non-zero will `foo` be called; otherwise, `bar` will be called.

Here's a short summary of some of the other language features that Phix offers
over Euphoria (just to name a few):

* [Data structures][9]
* [Classes][10]
* [Exception handling][11]
* [Associative arrays][12]

I'll have to admit, at first I just dismissed Phix as a knock-off of Euphoria,
but after doing some more research, I have to admit this Phix is definitely
worth further study!

If you'd like more information about this language, please see the
[Phix documentation][3].

[1]: http://phix.x10.mx/
[2]: https://github.com/petelomax/Phix
[3]: http://phix.x10.mx/docs/html/phix.htm
[4]: http://phix.x10.mx/docs/html/language.htm
[5]: https://en.wikipedia.org/wiki/Euphoria_(programming_language)
[6]: http://phix.x10.mx/docs/html/eucompat.htm
[7]: http://phix.x10.mx/docs/html/iff.htm
[8]: https://openeuphoria.org/docs/std_utils.html#_2216_iif
[9]: http://phix.x10.mx/docs/html/struct.htm
[10]: http://phix.x10.mx/docs/html/class.htm
[11]: http://phix.x10.mx/docs/html/try.htm
[12]: http://phix.x10.mx/docs/html/dict.htm


## Articles

- [Baklava in Phix](https://sampleprograms.io/projects/baklava/phix)
- [Hello World in Phix](https://sampleprograms.io/projects/hello-world/phix)