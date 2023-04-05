```rust
fn main(){println!("fn main(){{println!({0:?},{0:?})}}","fn main(){{println!({0:?},{0:?})}}")}
```

Let's break this down. In Rust, the `println!` function displays the desired text
with a newline. The first argument of `println!` is either an ordinary string or
a format string. If it is a format string, the subsequence arguments are values
to be formatted. Format string in Rust are rather complex and powerful. Let's take
a look at this particular one: `{0:?}`. This shows an item in its natural form.
For strings, this shows the string enclosed in double quotes. Since format strings
are enclosed in braces (`{}`), if you want to print a brace, you need to specify
the brace twice (``{{` or `}}`).

You'll notice that both the format string and the value to be formatted are
identical:

```
"fn main(){{println!({0:?},{0:?})}}"
```

In other words, we're using the format string to format itself! You'll notice
that the left side of that string is this:

```
fn main(){{println!(
```

That corresponds to the left-hand side of the program (keeping in mind that
`{{` results in `{`). The right-hand side of that string is this:

```
)}}
```

That corresponses to the right-hand side of the program (`}}` results in `}`).
If you put this all together, you get this output:

```rust
fn main(){println!("fn main(){{println!({0:?},{0:?})}}","fn main(){{println!({0:?},{0:?})}}")}
```

This is the same as the program. How cool is that?!

Anyway, I have to give credit where credit is due. I am a Rust newbie, and I
would be hard-pressed to come up with this on my own. I got this code
[here](https://cs.lmu.edu/~ray/notes/quineprograms/); scroll down the Rust
implementation. However, I learned a lot from this, and now I truly understand it
after writing this article.
