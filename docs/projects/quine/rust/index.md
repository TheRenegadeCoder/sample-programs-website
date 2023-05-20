---
title: Quine in Rust
layout: default
last-modified: 2023-04-05
featured-image: quine-in-rust.jpg
tags: [rust, quine]
authors:
  - rzuckerm

---

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
fn main(){println!("fn main(){{println!({0:?},{0:?})}}","fn main(){{println!({0:?},{0:?})}}")}
```

{% endraw %}

[Quine](https://sampleprograms.io/projects/quine) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's break this down. In Rust, the `println!` function displays the desired text
with a newline. The first argument of `println!` is either an ordinary string or
a format string. If it is a format string, the subsequent arguments are values
to be formatted. Format strings in Rust are rather complex and powerful. If you
want to learn more about this, see the
[official Rust documentation](https://doc.rust-lang.org/std/fmt/).

Let's take at look at this particular one: 

{% raw %}
```
{0:?}
```
{% endraw %}

* All format strings are enclosed in braces `{}`.
* `0` means the first (zeroth in 0-based counting) argument after the format
  string.
* `:?` shows an item in its natural form. For strings, this shows the value
  enclosed in double quotes.

You'll notice that both the format string and the value to be formatted are
identical:

{% raw %}
```
"fn main(){{println!({0:?},{0:?})}}"
```
{% endraw %}

In other words, we're using the format string to format itself! Notice that
these characters are used in this format string:

{% raw %}
* `{{`
* `}}`
{% endraw %}

These display like this, respectively:

{% raw %}
* `{`
* `}`
{% endraw %}

The braces have to be doubled up since, as mentioned above, all format string
are enclosed in braces.

Notice that the left side of that string is this:

{% raw %}
```
fn main(){{println!(
```
{% endraw %}

That corresponds to the left-hand side of the program. The right-hand side of
that string is this:

{% raw %}
```
)}}
```
{% endraw %}

That corresponds to the right-hand side of the program. If you put this all
together, you will get this output:

{% raw %}
```rust
fn main(){println!("fn main(){{println!({0:?},{0:?})}}","fn main(){{println!({0:?},{0:?})}}")}
```
{% endraw %}

This is the same as the program. How cool is that?!

Anyway, I have to give credit where credit is due. I am a Rust newbie, and I
would be hard-pressed to come up with this on my own. I got this code
[here](https://cs.lmu.edu/~ray/notes/quineprograms/); scroll down the Rust
implementation. However, I learned a lot from this, and now I truly understand it
after writing this article.


## How to Run the Solution

If you want to run this program, you'll first need to download a
copy of the 
[Rust compiler](https://www.rust-lang.org/tools/install),
and follow the installation instructions. From there, open a terminal, and
run this command:

```
rustc quine.rs
./quine
```
