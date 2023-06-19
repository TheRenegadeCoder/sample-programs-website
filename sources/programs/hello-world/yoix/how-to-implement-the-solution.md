Yoix requires you to import every system function that you use. All the
`import` statements start with `yoix`, followed by the module where the
function is located, followed by the function name. Since `printf` is in
the `stdio` module, the `import` statement is `yoix.stdio.printf`.
The `printf` statement is same as Java, which is not surprising since
[the Yoix interpreter runs in Java][1].

[1]: https://en.wikipedia.org/wiki/Yoix
