At long last, let's take a stab at Hello World in Hack.

Although Hack is derived from PHP, this code looks quite
different than PHP. The first thing you'll notice is this:

```hack
<<__EntryPoint>>
```

The `<<...>>` is how Hack defines an attribute. The
[`__EntryPoint` attribute][1] defines a top-level function
where execution is started. That function is `main`, but it
does not have to be called `main`. Any function with the
`__EntryPoint` attribute will be considered the top-level
function.

Next, the `main` function is defined. For this sample program,
there are no command-line arguments to process, so no arguments are
needed. The function does not return anything, so the return type
is `void`.

Finally, there is the `echo` statement, which is exactly the same
as Hello World in PHP. However, I will point out that you can't mix
HTML with Hack like you can with PHP, so that's one of the biggest 
syntactic differences. Otherwise, both languages perform a similar 
function: backend web development.

[1]: https://docs.hhvm.com/hack/attributes/predefined-attributes#__entrypoint
