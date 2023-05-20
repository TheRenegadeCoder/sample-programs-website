---
title: Hello World in Perl
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-perl.jpg
tags: [perl, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Perl](https://sampleprograms.io/languages/perl) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```perl
print "Hello, World!";
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Perl](https://sampleprograms.io/languages/perl) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Without further ado, let's dive straight into our implementation 
of Hello World in Perl.

Well, that was anticlimactic. In fact, it was about as disappointing 
as our implementations of Hello World in Python and Ruby. That said, 
who doesn't love a simple implementation (talking to you, Java).

At any rate, let's dig into this a little bit. For starters, we'll 
notice there are no parentheses required for Perl's print function. 
I use the word "required" because we can actually call print with them:

```perl
print("Hello, World!");
```

However, from my understanding, it's good Perl style to omit the parentheses 
for built-in functions.

Oh, I should probably clarify something. In Perl, they're not called 
functions. Instead, they're called subroutines, and you can declare one 
of your own using the sub keyword. That's a new one for me!


## How to Run the Solution

As usual, we can try the solution using an [online Perl interpreter][1]. All we 
have to do is drop the code into the editor and hit run.

As an alternative, we can always run Perl locally. First, we'll need to get 
the latest version of Perl from the [official website][2]. After that, we should 
probably get a copy of the solution. Assuming Perl is now in our path, we can 
get to work:

```shell
perl hello-world.pl
```

Since Perl is a scripting language, we can quickly run the script with the 
command above. If successful, "Hello, World!" should print to the console.

[1]: https://www.onlinegdb.com/online_perl_compiler
[2]: https://www.perl.org/get.html
