---
title: Hello World in Rust
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-rust.jpg
tags: [rust, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
fn main() {
    println!("Hello, World!");
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

In fact, Rust's implementation is even easier. There's no need to import
any IO packages to get access to _println_. We just need to create our `main`
function, add our print code, and we're done.

But, wait a minute. That __print line__ seems a little off. What's with the bang `!`?
To be honest, I had to do a bit of digging for this. As it turns out, _println_ is
not a function at all. __It's a built-in macro__. That's a new term for me, so let's
learn a little more about it.

According to [the Rust Programming Language book][2], macros are a language feature
that allow you to abstract syntax. In other words, macros allow you to do some
metaprogramming by adding grammar to Rust's abstract syntax tree. Perhaps an example
would make more sense:

{% raw %}
```rust
macro_rules! println {
    () => {
        $crate::print!("\n")
    };
    ($($arg:tt)*) => {{
        $crate::io::_print($crate::format_args_nl!($($arg)*));
    }};
}
```
{% endraw %}

This is the actual [definition of the _println_ macro in Rust][3] (click on "source").
I won't go into exactly what's happening, but basically we have defined two available patterns
for _println_: empty and variable arguments. Rust functions don't
have support for variable arguments, so you can add the functionality with macros.

That said, I'm only just learning macros for the first time, so I recommend an
article by Kasper Andersen called [why Rust has macros][4]. It's quite thorough,
and I think it does a better job than Rust's documentation.

[2]: https://doc.rust-lang.org/book/
[3]: https://doc.rust-lang.org/std/macro.println.html
[4]: https://kasma1990.gitlab.io/2018/03/04/why-rust-has-macros/


## How to Run the Solution

As always, we can try out this code using an [online Rust compiler][5]. All we
need to do is drop the code into the editor and hit run.

Alternatively, we can [download the latest Rust compiler][6] and a [copy of the solution][7].
Then, assuming the compiler is in the path, navigate to folder with the solution and run
the following in Windows:

```console
rustc hello-world.rs
hello-world.exe
```

Of course, in Unix-based environments, the following will run the new binary:

```console
./hello-world
```

And, that's it! "Hello, World!" should print directly to the console.

[5]: https://play.rust-lang.org/
[6]: https://www.rust-lang.org/tools/install
[7]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/r/rust/hello-world.rs
